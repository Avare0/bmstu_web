from rest_framework.views import *
from rest_framework.response import Response
from ..serializers import *

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..repositories.UsersRepository import UsersRepository
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from django.contrib.auth.hashers import make_password

RESPONSE_FORMAT = {
    'status': 'success',
    'data': None,
    'message': None
}
class UsersView(APIView):

    repository = UsersRepository()
    @swagger_auto_schema(operation_summary='Create new user',
                         operation_description='Create new user',
                         responses={
                             '200': openapi.Response('Successfully created new user', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_OBJECT, description='data')
                                 })),
                             '400': openapi.Response('Invalid input data', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_OBJECT, description='data')
                                 })),
                         },
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             properties={
                                 'username': openapi.Schema(type='string', description='username'),
                                 'password': openapi.Schema(type='string', description='password'),
                                 'sex': openapi.Schema(type='string', description='sex'),
                                 'type': openapi.Schema(type='string', description='type'),
                                 'city_id': openapi.Schema(type='string', description='city_id'),
                                 'first_name': openapi.Schema(type='string', description='first_name'),
                                 'last_name': openapi.Schema(type='string', description='last_name'),
                                'photo': openapi.Schema(type='file', description='photo'),
                                 'email': openapi.Schema(type='string', description='email')
                             },
                         )
                         )
    def post(self, request):
        resp = RESPONSE_FORMAT.copy()
        code = 200
        serialized = UserSerializer2(data=request.data)
        if serialized.is_valid():
            d = dict(serialized.data)
            photoes = request.FILES.getlist('photo')
            d['password'] = make_password(serialized.data['password'])
            d['photo'] = photoes[0]
            user = self.repository.create(**d)
            if user:
                return Response(data=resp, status=code)
        else:
            resp['status'] = 'error'
            resp['message'] = serialized.errors
            code = 400
            return Response(data=resp, status=code)

    @swagger_auto_schema(operation_summary='Get info about user',
                         operation_description='Get info about user',
                         responses={
                             '200': openapi.Response('Info about user', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             properties={
                                 'id': openapi.Schema(type='integer', description='id'),
                                 'username': openapi.Schema(type='string', description='username'),
                                 'sex': openapi.Schema(type='string', description='sex'),
                                 'type': openapi.Schema(type='string', description='type'),
                                 'city': openapi.Schema(type='string', description='city_id'),
                                 'first_name': openapi.Schema(type='string', description='first_name'),
                                 'last_name': openapi.Schema(type='string', description='last_name'),
                                 'photo': openapi.Schema(type='file', description='photo'),
                                 'email': openapi.Schema(type='string', description='email')
                             },
                         )
                                 })),
                             '400': openapi.Response('Invalid input data', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_OBJECT, description='data')
                                 })),
                         },
                         manual_parameters=[openapi.Parameter(name='user_id', type='integer', in_=openapi.IN_QUERY)]
                         )
    def get(self, request):
        resp = RESPONSE_FORMAT.copy()
        code = 200

        if 'id' in request.GET:
            data = self.repository.filter(id=int(request.GET['id']))[0]
            data = UserSerializer(data)
            resp['data'] = data
            return Response(data=resp, status=code)

        resp['status'] = 'error'
        resp['message'] = 'Not such method exists'
        code = 400
        return Response(data=resp, status=code)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairViewSerializer

    @swagger_auto_schema(operation_summary='Get JWT tokens',
                         operation_description='Get JWT tokens',
                         responses={
                             '200': openapi.Response('Successfully created tokens', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_OBJECT, description='data', properties={
                                         'access': openapi.Schema(type=openapi.TYPE_STRING, description='access token'),
                                         'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='refresh token')
                                     })
                                 })),
                             '401': openapi.Response('Invalid credentials', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_OBJECT, description='data')
                                 })),
                         },
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             properties={
                                 'username': openapi.Schema(type='string'),
                                 'password': openapi.Schema(type='string', description='`House description'),
                             },
                         ))
    def post(self, request,*args, **kwargs):
        return super().post(request)

class MyTokenRefreshView(TokenRefreshView):

    @swagger_auto_schema(operation_summary='Refresh JWT token',
                         operation_description='Refresh JWT token',
                         responses={
                             '200': openapi.Response('Successfully updated token', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_OBJECT, description='data', properties={
                                         'access': openapi.Schema(type=openapi.TYPE_STRING, description='access token'),
                                     })
                                 })),
                             '400': openapi.Response('Invalid credentials', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_OBJECT, description='data')
                                 })),
                         },
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             properties={
                                 'refresh': openapi.Schema(type='string'),
                             },
                         ))
    def post(self, request, *args, **kwargs):
        return super().post(request)