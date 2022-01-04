from rest_framework.views import *
from rest_framework.response import Response
from ..serializers import *

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..repositories.CitiesRepository import CitiesRepository

RESPONSE_FORMAT = {
    'status': 'success',
    'data': None,
    'message': None
}

class CitiesView(APIView):
    response = openapi.Response('List of all cities', CitiesSerializer)
    repository = CitiesRepository()
    @swagger_auto_schema(operation_summary='Get list of all cities',
                         operation_description='Get list of all cities with info about them',
                         responses={
                             '200': openapi.Response('List of all cities', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(
                                         type=openapi.TYPE_ARRAY,
                                         items=openapi.Schema(
                                             type=openapi.TYPE_OBJECT,
                                             properties={
                                                 'name': openapi.Schema(type=openapi.TYPE_STRING,
                                                                        description='name of the city'),
                                                 'country': openapi.Schema(
                                                     type=openapi.TYPE_OBJECT,
                                                     properties={
                                                         'name': openapi.Schema(type=openapi.TYPE_STRING,
                                                                                description='name of the country')}
                                                 )
                                             }
                                         )
                                     )
                                 }))
                         })
    def get(self, request, *args, **kwargs):
        resp = RESPONSE_FORMAT.copy()
        code = 200
        cities = self.repository.all()
        cities = CitiesSerializer(cities, many=True).data

        resp['data'] = cities

        return Response(data=resp, status=code)