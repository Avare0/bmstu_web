from rest_framework.permissions import IsAuthenticated
from rest_framework.views import *
from rest_framework.response import Response
from ..serializers import *

from datetime import datetime
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..repositories.HousesRepository import HousesRepository
from ..repositories.OrdersRepository import OrdersRepository
RESPONSE_FORMAT = {
    'status': 'success',
    'data': None,
    'message': None
}

class OrdersView(APIView):
    repository = OrdersRepository()
    permission_classes = [IsAuthenticated]
    house_repository = HousesRepository()


    @swagger_auto_schema(operation_summary='Create new order',
                         operation_description='Create order for a special house',
                         responses={
                             '200': openapi.Response('Successfully created new order', schema=openapi.Schema(
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
                                 'date_from': openapi.Schema(type='string', description='date_from format yyyy-mm-dd'),
                                 'date_till': openapi.Schema(type='string', description='date_till format yyyy-mm-dd'),
                                 'guests_amount': openapi.Schema(type='integer', description='guests_amount'),
                                 'house_id': openapi.Schema(type='integer', description='house id'),
                             },
                         )
                         )
    def post(self, request):
        """
        Create order
        """
        resp = RESPONSE_FORMAT.copy()
        code = 200

        try:
            date_from = datetime.fromisoformat(request.data['date_from'])
            date_till = datetime.fromisoformat(request.data['date_till'])
        except:
            resp['status'] = 'error'
            resp['message'] = 'Incorrect dates, they should be in format yyyy-mm-dd'
            code = 400
            return Response(data=resp, status=code)

        if int(request.data['house_id']) not in list(map(int, list(self.house_repository.values_list('id', flat=True)))):
            resp['status'] = 'error'
            resp['message'] = 'No house with such id'
            code = 400
            return Response(data=resp, status=code)

        house = self.house_repository.filter(id=int(request.data['house_id']))[0]

        if house.guests_amount < int(request.data['guests_amount']):
            resp['status'] = 'error'
            resp['message'] = 'Amount of guests is more than maximum amount'
            code = 400
            return Response(data=resp, status=code)




        if self.repository.check_availiable_date(date_from, date_till, int(request.data['house_id'])):
            self.repository.create(
                house_id=int(request.data['house_id']),
                user=request.user,
                date_from=request.data['date_from'],
                date_till=request.data['date_till'],
                guests_amount=int(request.data['guests_amount'])
            )
        else:
            resp['status'] = 'error'
            resp['message'] = 'These dates are unavailable'
            code = 400
            return Response(data=resp, status=code)
        return Response(data=resp, status=code)

    @swagger_auto_schema(operation_summary='Get user or owner orders',
                         operation_description='Get user or owner orders',
                         responses={
                             '200': openapi.Response('List of orders', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_OBJECT, description='data')
                                 })),
                             '403': openapi.Response('request user_id is different from user_id in query params', schema=openapi.Schema(
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
                         manual_parameters=[openapi.Parameter(name='owner_id', in_=openapi.IN_QUERY, type='integer'),
                                            openapi.Parameter(name='user_id', in_=openapi.IN_QUERY, type='integer'),]
                         )
    def get(self, request):
        resp = RESPONSE_FORMAT.copy()
        code = 200

        if 'user_id' in request.GET:
            if int(request.GET['user_id']) != request.user.id:
                resp['status'] = 'error'
                resp['message'] = 'Only user with this id can access this'
                code = 403
                return Response(data=resp, status=code)
            data = self.repository.filter(user_id=int(request.GET['user_id']))
            # raise KeyError(data)
            data = OrdersSerializer(data, many=True).data
            resp['data'] = data
            return Response(data=resp, status=code)
        elif 'owner_id' in request.GET:
            orders = self.repository.get_all_owner_orders(request.GET['owner_id'])
            if int(request.GET['owner_id']) != request.user.id:
                resp['status'] = 'error'
                resp['message'] = 'Only user with this id can access this'
                code = 403
                return Response(data=resp, status=code)

            data = OrdersSerializer(orders, many=True).data
            resp['data'] = data
            return Response(data=resp, status=code)
        elif 'house_id' in request.GET:
            orders = self.repository.filter(house_id=int(request.GET['house_id']))

            data = OrdersSerializer(orders, many=True).data
            resp['data'] = data
            return Response(data=resp, status=code)
        code = 404
        resp['status'] = 'error'
        resp['message'] = 'Incorrect query params or no params passed'
        return Response(data=resp, status=code)


