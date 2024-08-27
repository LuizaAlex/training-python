from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
from task02.src.commons import RESPONSE_BAD_REQUEST_CODE, RESPONSE_OK_CODE, build_response, raise_error_response
from task02.src.commons.exception import ApplicationException

_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        # Pentru simplificare, considerăm că cererea este validă dacă calea și metoda sunt corecte
        errors = {}
        path = event.get('rawPath', '')
        method = event.get('requestContext', {}).get('http', {}).get('method', '')
        
        if method not in ["GET"]:
            errors["method"] = "Unsupported HTTP method"
        if path not in ["/hello", "/"]:
            errors["path"] = "Unsupported path"
        
        return errors

    def handle_request(self, event, context):
        path = event.get('rawPath', '/')
        method = event.get('requestContext', {}).get('http', {}).get('method', 'GET')
        
        if path == "/hello" and method == "GET":
            response = {
                "statusCode": 200,
                "message": "Hello from Lambda"
            }
        else:
            response = {
                "statusCode": 400,
                "message": f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
            }
        
        return build_response(content=response, code=response['statusCode'])

HANDLER = HelloWorld()

def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
