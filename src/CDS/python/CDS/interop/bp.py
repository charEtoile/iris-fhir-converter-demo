from fastapi import HTTPException
from CDS.hapi_calculator import calculate_risk
from iop import BusinessProcess
from CDS.models import RiskAssessmentInput, RiskCalculationResult
from CDS.interop.msg import RiskAssessmentInputRequest, RiskAssessmentResultResponse
from pydantic import ValidationError


class BP(BusinessProcess):
    def on_risk_assessment_input_request_message(self, request: RiskAssessmentInputRequest)->RiskAssessmentResultResponse:
        result: RiskCalculationResult = self._calculate_hapi_risk(request.input)
        response = RiskAssessmentResultResponse(result=result)
        return response

    def _calculate_hapi_risk(self, input_data: RiskAssessmentInput):
        """
        Calculate Hospital Acquired Pressure Injury (HAC PI) risk.
        
        Uses the Reese et al. (2024) validated logistic regression model to compute
        pressure injury risk from patient demographics, clinical measurements, Braden 
        Scale assessments, medical devices, and clinical conditions.
        
        **Algorithm**: Logistic regression with 35+ coefficients
        - Z = intercept + Σ(coefficient_i * variable_i)  
        - P = 1 / (1 + exp(-Z))
        - 95% CI computed via Delta method
        
        **Performance**: <100ms calculation time
        
        **Stateless**: No data persistence, suitable for real-time clinical use
        
        Args:
            input_data: Patient assessment data (age required, other fields optional with defaults)
        
        Returns:
            RiskCalculationResult with risk percentage, 95% CI, Z-score, category, and color
        
        Raises:
            HTTPException 422: Validation error (invalid input data)
            HTTPException 500: Internal calculation error
        """
        try:
            result = calculate_risk(input_data)
            return result
            
        except ValidationError as e:
            raise HTTPException(
                status_code=422,
                detail=f"Validation error: {str(e)}"
            )
        
        except ValueError as e:
            raise HTTPException(
                status_code=422,
                detail=f"Invalid input data: {str(e)}"
            )
        
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Risk calculation failed: {str(e)}"
            )


