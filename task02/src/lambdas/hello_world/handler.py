from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
from task02.src.commons import RESPONSE_BAD_REQUEST_CODE, RESPONSE_OK_CODE, build_response, raise_error_response
from task02.src.commons.exception import ApplicationException

_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
           
        path = event.get("path", "")
        method = event.get("httpMethod", "")

        if method == "GET" and path == "/hello":
            return {}
        else:
            raise_error_response(
                RESPONSE_BAD_REQUEST_CODE,
                f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
            )

        
    def handle_request(self, event, context):
        """
        Handles the incoming request after validation.
        """
        self.validate_request(event)  # Validarea cererii

        # Returnarea răspunsului OK pentru /hello
        message = "Hello from Lambda"
        return build_response({"message": message}, RESPONSE_OK_CODE)  

HANDLER = HelloWorld()


def lambda_handler(event, context):
    try:
        return HANDLER.lambda_handler(event=event, context=context)
    except ApplicationException as e:
        return {
            'statusCode': e.code,
            'body': e.content
        }
