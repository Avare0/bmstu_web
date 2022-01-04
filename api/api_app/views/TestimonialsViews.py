from rest_framework.permissions import IsAuthenticated
from rest_framework.views import *
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..serializers import TestimonialsSerializer

from ..repositories.HousesRepository import HousesRepository
from ..repositories.TestimonialsRepository import TestimonialsRepository

RESPONSE_FORMAT = {
    'status': 'success',
    'data': None,
    'message': None
}
class TestimonialCreateView(APIView):

    repository = TestimonialsRepository()
    house_repository = HousesRepository()
    @swagger_auto_schema(operation_summary='Create new testimonial',
                         operation_description='Create testimonial for a special house',
                         responses={
                             '200': openapi.Response('Successfully created new testimonial', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_OBJECT, description='data')
                                 })),
                             '404': openapi.Response('House not found', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_OBJECT, description='data')
                                 })),
                             '401': openapi.Response('Unauthorized', schema=openapi.Schema(
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
                                 'text': openapi.Schema(type='string', description='testimonial text'),
                             },
                         )
                         )
    def post(self, request, pk):
        resp = RESPONSE_FORMAT.copy()
        code = 200

        if int(pk) not in list(map(int, list(self.house_repository.values_list('id', flat=True)))):
            resp['status'] = 'error'
            resp['message'] = 'No house with such id'
            code = 400
            return Response(data=resp, status=code)
        if not request.user.is_authenticated:
            resp['status'] = 'error'
            resp['message'] = 'Unauthorized'
            code = 401
            return Response(data=resp, status=code)
        self.repository.create(
            house_id=int(pk),
            user=request.user,
            text=request.data['text']
        )

        return Response(data=resp, status=code)

    def get(self, request, pk):
        resp = RESPONSE_FORMAT.copy()

        objects = self.repository.filter(house_id=pk)
        serialized = TestimonialsSerializer(objects, many=True)

        code = 200
        resp['data'] = serialized.data
        return Response(data=resp, status=code)
