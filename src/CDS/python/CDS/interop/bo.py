from iop import BusinessOperation

class BO(BusinessOperation):
    def on_http_request(self, message_request: str)->str:
        response: str = "Not implemented"
        return response