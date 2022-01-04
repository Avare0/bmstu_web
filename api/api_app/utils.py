from rest_framework.views import exception_handler
from rest_framework.response import Response
RESPONSE_FORMAT = {
    'status': 'success',
    'data': None,
    'message': None
}

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    # Now add the HTTP status code to the response.
    if response is not None:
        resp = RESPONSE_FORMAT.copy()
        resp['message'] = response.data if 'detail' not in response.data.keys() else response.data['detail']
        resp['status'] = 'error'
        code = response.status_code
        response = Response(data=resp, status=code, headers=response.headers)

    return response
def jwt_response_payload_handler(token, user=None, request=None):
    response = exception_handler(exc, context)
    if response is not None:
        resp = RESPONSE_FORMAT.copy()
        resp['message'] = response.data if 'detail' not in response.data.keys() else response.data['detail']
        resp['status'] = 'success'
        code = response.status_code
        resp['data'] = {
            **token,
            'user': {
                'username': user.username,
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'photo': user.photo
            }
        }
        response = Response(data=resp, status=code, headers=response.headers)
    return response