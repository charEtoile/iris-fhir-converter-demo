from iop import Message, PydanticMessage
from CDS.models import RiskAssessmentInput, RiskCalculationResult
from dataclasses import dataclass


@dataclass
class HttpMessageRequest(Message):
    method: str
    url: str
    headers: dict
    body: str

@dataclass
class HttpMessageResponse(Message):
    status: int
    headers: dict
    body: str

# No @dataclass decorator: IOP's _serialization.py explicitly raises SerializationError
# when a class combines @dataclass with PydanticMessage (a BaseModel subclass).
# Serialization is handled via model_dump_json()/model_validate_json() — no dataclass needed.
class RiskAssessmentInputRequest(PydanticMessage):
    input: RiskAssessmentInput

# Same reason as RiskAssessmentInputRequest: @dataclass + PydanticMessage is forbidden by IOP.
class RiskAssessmentResultResponse(PydanticMessage):
    result: RiskCalculationResult