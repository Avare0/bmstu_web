from rest_framework.permissions import IsAuthenticated

from rest_framework.views import *
from rest_framework.response import Response
from ..permissions import *
from ..serializers import *

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view

from ..repositories.HousesRepository import HousesRepository
from ..repositories.FacilitiesRepository import FacilitiesRepository
from ..repositories.HousePhotosRepository import HousesPhotosRepository
from ..repositories.HouseFaciltiiesRepository import HousesFacilitiesRepository

RESPONSE_FORMAT = {
    'status': 'success',
    'data': None,
    'message': None
}
class HousesView(APIView):
    serializer_class = HousesSerializer
    house_repository = HousesRepository()
    facilities_repository = FacilitiesRepository()
    house_facilities_repository = HousesFacilitiesRepository()
    photos_repository = HousesPhotosRepository()
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary='Get list of all houses',
                         operation_description='Get list of all houses',
                         responses={
                             '200': openapi.Response('List of all houses', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_ARRAY, description='data',
                                                            items=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                                                                'name': openapi.Schema(type='string'),
                                                                'desc': openapi.Schema(type='string',
                                                                                       description='House description'),
                                                                'city': openapi.Schema(
                                                                    type=openapi.TYPE_OBJECT,
                                                                    properties={
                                                                        'name': openapi.Schema(type=openapi.TYPE_STRING,
                                                                                               description='name of the city'),
                                                                        'country': openapi.Schema(
                                                                            type=openapi.TYPE_OBJECT,
                                                                            properties={
                                                                                'name': openapi.Schema(
                                                                                    type=openapi.TYPE_STRING,
                                                                                    description='name of the country')}
                                                                        )
                                                                    }
                                                                ),
                                                                'guests_amount': openapi.Schema(type='integer',
                                                                                                description='Maximum amount of guests'),
                                                                'beds_amount': openapi.Schema(type='integer',
                                                                                              description='Amount of beds'),
                                                                'owner': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                                                                    'first_name': openapi.Schema(type='string'),
                                                                    'second_name': openapi.Schema(type='string'),
                                                                    'photo': openapi.Schema(type='string')
                                                                }),
                                                                'address': openapi.Schema(type='string',
                                                                                          description='House address'),
                                                                'rules': openapi.Schema(type='string',
                                                                                        description='House rules'),
                                                                'bathroom_amount': openapi.Schema(type='integer',
                                                                                                  description='Bathroom amount'),
                                                                'house_facilities': openapi.Schema(
                                                                    type=openapi.TYPE_ARRAY,
                                                                    items=openapi.Schema(
                                                                        type=openapi.TYPE_OBJECT,
                                                                        properties={
                                                                            'facility': openapi.Schema(
                                                                                type=openapi.TYPE_OBJECT,
                                                                                description='link to the photo',
                                                                                properties={
                                                                                    'id': openapi.Schema(type='integer',
                                                                                                         description='facility id'),
                                                                                    'name': openapi.Schema(
                                                                                        type='string',
                                                                                        description='facility name'),
                                                                                    'file': openapi.Schema(
                                                                                        type='string',
                                                                                        description='facility link'),

                                                                                }),
                                                                            'id': openapi.Schema(type='integer',
                                                                                                 description='house facility id'),
                                                                            'house': openapi.Schema(type='integer',
                                                                                                    description='house id')

                                                                        }
                                                                    )),
                                                                'house_photo': openapi.Schema(type=openapi.TYPE_ARRAY,
                                                                                              items=openapi.Schema(
                                                                                                  type=openapi.TYPE_OBJECT,
                                                                                                  properties={
                                                                                                      'photo': openapi.Schema(
                                                                                                          type=openapi.TYPE_STRING,
                                                                                                          description='link to the photo'),

                                                                                                  }
                                                                                              )),
                                                                'testimonials_house': openapi.Schema(
                                                                    type=openapi.TYPE_ARRAY,
                                                                    items=openapi.Schema(
                                                                        type=openapi.TYPE_OBJECT,
                                                                        properties={
                                                                            'text': openapi.Schema(
                                                                                type=openapi.TYPE_STRING,
                                                                                description='testimonial text'),
                                                                            'house_id': openapi.Schema(
                                                                                type=openapi.TYPE_INTEGER,
                                                                                description='house id'),
                                                                            'date': openapi.Schema(
                                                                                type=openapi.TYPE_STRING,
                                                                                description='testimonial date'),
                                                                            'user_id': openapi.Schema(
                                                                                type=openapi.TYPE_INTEGER,
                                                                                description='testimonial user'),

                                                                        }
                                                                    )),
                                                            }))
                                 }, description='List of all houses')),
                         },
                         manual_parameters=[openapi.Parameter(name='user_id', in_=openapi.IN_QUERY, type='integer')]
                         )
    def get(self, request, *args, **kwargs):
        resp = RESPONSE_FORMAT.copy()
        if 'user_id' in request.GET:
            if int(request.GET['user_id']) != request.user.id:
                resp['status'] = 'error'
                resp['message'] = 'Only user with this id can access this'
                code = 403
                return Response(data=resp, status=code)
            objects = self.house_repository.filter(owner_id=request.GET['user_id'])
        else:
            objects = self.house_repository.all()
        serialized = HousesSerializer(objects, many=True)

        code = 200
        resp['data'] = serialized.data
        return Response(data=resp, status=code)

    @swagger_auto_schema(operation_summary='Create a house',
                         operation_description='Create a house',
                         responses={
                             '200': openapi.Response('Success creating an object', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_INTEGER, description='data')
                                 })),
                             '400': openapi.Response('Incorrect input data', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_INTEGER, description='data')
                                 }))
                         },
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             properties={
                                 'name': openapi.Schema(type='string'),
                                 'desc': openapi.Schema(type='string', description='`House description'),
                                 'city_id': openapi.Schema(type='integer', description='House city id'),
                                 'guests_amount': openapi.Schema(type='integer',
                                                                 description='Maximum amount of guests'),
                                 'beds_amount': openapi.Schema(type='integer', description='Amount of beds'),
                                 'address': openapi.Schema(type='string', description='House address'),
                                 'rules': openapi.Schema(type='string', description='House rules'),
                                 'bathroom_amount': openapi.Schema(type='integer', description='Bathroom amount'),
                                 'facility': openapi.Schema(type=openapi.TYPE_STRING, description='House facilities'),
                                 'photoes': openapi.Schema(type=openapi.TYPE_FILE, description='House photoes')
                             },
                         ),
                         )
    def post(self, request):
        resp = RESPONSE_FORMAT.copy()
        code = 200

        facilities = list(map(int, request.POST.getlist('facility')))
        photoes = request.FILES.getlist('photo')

        # request.data.pop('facility')
        # request.data.pop('photo')

        # request.data['owner'] = request.user.id
        form = HouseCreateSerializer(data=request.data)

        availiable_facilities = set(self.facilities_repository.values_list('id'))

        if len(availiable_facilities.intersection(set(facilities))) < len(facilities):
            resp['status'] = 'error'
            resp['message'] = f'Invalid facility ids'
            code = 400
            return Response(data=resp, status=code)

        if not form.is_valid():
            resp['status'] = 'error'
            resp['message'] = f'Invalid data in house information'
            code = 400
            return Response(data=resp, status=code)

        data = dict(form.data)
        city = data.pop('city')
        owner = data.pop('owner')
        data['city_id'] = city
        data['owner_id'] = request.user.id
        obj = self.house_repository.create(**data)

        for id in facilities:
            self.house_facilities_repository.create(
                house_id=obj.id,
                facility_id=id
            )
        for photo in photoes:
            self.photos_repository.create(
                house_id=obj.id,
                photo=photo
            )

        return Response(data=resp, status=code)

class HouseView(APIView):
    repository = HousesRepository()

    @swagger_auto_schema(operation_summary='Get information about the house',
                         operation_description='Get information about the house',
                         responses={
                             '200': openapi.Response('Ingo about the house', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data':openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                                                                'name': openapi.Schema(type='string'),
                                                                'desc': openapi.Schema(type='string',
                                                                                       description='House description'),
                                                                'city': openapi.Schema(
                                                                    type=openapi.TYPE_OBJECT,
                                                                    properties={
                                                                        'name': openapi.Schema(type=openapi.TYPE_STRING,
                                                                                               description='name of the city'),
                                                                        'country': openapi.Schema(
                                                                            type=openapi.TYPE_OBJECT,
                                                                            properties={
                                                                                'name': openapi.Schema(
                                                                                    type=openapi.TYPE_STRING,
                                                                                    description='name of the country')}
                                                                        )
                                                                    }
                                                                ),
                                                                'guests_amount': openapi.Schema(type='integer',
                                                                                                description='Maximum amount of guests'),
                                                                'beds_amount': openapi.Schema(type='integer',
                                                                                              description='Amount of beds'),
                                                                'owner': openapi.Schema(type=openapi.TYPE_OBJECT,
                                                                                        properties={
                                                                                            'first_name': openapi.Schema(
                                                                                                type='string'),
                                                                                            'second_name': openapi.Schema(
                                                                                                type='string'),
                                                                                            'photo': openapi.Schema(
                                                                                                type='string')
                                                                                        }),
                                                                'address': openapi.Schema(type='string',
                                                                                          description='House address'),
                                                                'rules': openapi.Schema(type='string',
                                                                                        description='House rules'),
                                                                'bathroom_amount': openapi.Schema(type='integer',
                                                                                                  description='Bathroom amount'),
                                                                'house_facilities': openapi.Schema(
                                                                    type=openapi.TYPE_ARRAY,
                                                                    items=openapi.Schema(
                                                                        type=openapi.TYPE_OBJECT,
                                                                        properties={
                                                                            'facility': openapi.Schema(
                                                                                type=openapi.TYPE_OBJECT,
                                                                                description='link to the photo',
                                                                                properties={
                                                                                    'id': openapi.Schema(type='integer',
                                                                                                         description='facility id'),
                                                                                    'name': openapi.Schema(
                                                                                        type='string',
                                                                                        description='facility name'),
                                                                                    'file': openapi.Schema(
                                                                                        type='string',
                                                                                        description='facility link'),

                                                                                }),
                                                                            'id': openapi.Schema(type='integer',
                                                                                                 description='house facility id'),
                                                                            'house': openapi.Schema(type='integer',
                                                                                                    description='house id')

                                                                        }
                                                                    )),
                                                                'house_photo': openapi.Schema(type=openapi.TYPE_ARRAY,
                                                                                              items=openapi.Schema(
                                                                                                  type=openapi.TYPE_OBJECT,
                                                                                                  properties={
                                                                                                      'photo': openapi.Schema(
                                                                                                          type=openapi.TYPE_STRING,
                                                                                                          description='link to the photo'),

                                                                                                  }
                                                                                              )),
                                                                'testimonials_house': openapi.Schema(
                                                                    type=openapi.TYPE_ARRAY,
                                                                    items=openapi.Schema(
                                                                        type=openapi.TYPE_OBJECT,
                                                                        properties={
                                                                            'text': openapi.Schema(
                                                                                type=openapi.TYPE_STRING,
                                                                                description='testimonial text'),
                                                                            'house_id': openapi.Schema(
                                                                                type=openapi.TYPE_INTEGER,
                                                                                description='house id'),
                                                                            'date': openapi.Schema(
                                                                                type=openapi.TYPE_STRING,
                                                                                description='testimonial date'),
                                                                            'user_id': openapi.Schema(
                                                                                type=openapi.TYPE_INTEGER,
                                                                                description='testimonial user'),

                                                                        }
                                                                    )),
                                                            })
                                 }, description='List of user houses')),
                             '404': openapi.Response('No house with such id', schema=openapi.Schema(type='object', properties={
                                 'status': openapi.Schema(type='string'),
                                 'message': openapi.Schema(type='string'),
                                 'data': openapi.Schema(type='object')
                             }, description='Invalid house id'))
                         },
                         )
    def get(self, request, *args, **kwargs):
        resp = RESPONSE_FORMAT.copy()
        code = 200
        house = self.repository.filter(id=self.kwargs['pk'])

        if len(house) > 0:
            house = HousesSerializer(house[0]).data
            resp['data'] = house
        else:
            resp['status'] = 'error'
            resp['message'] = 'No house with such id'
            code = 404
        return Response(status=code, data=resp)

    @swagger_auto_schema(operation_summary='Delete a house',
                         operation_description="Delete a house",
                         responses={
                             '200': openapi.Response('Object deleted', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_INTEGER, description='data')
                                 }, description='Success deleting an object')),
                             '404': openapi.Response('No house with such id', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_INTEGER, description='data')
                                 }, description='No house with such id')),
                             '401': openapi.Response('Unauthorized', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_INTEGER, description='data')
                                 }, description='Unauthorized')),
                             '403': openapi.Response('Not the owner of the house', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_INTEGER, description='data')
                                 }, description='Not the owner of the house'))
                         },
                         )
    def delete(self, request, *args, **kwargs):
        resp = RESPONSE_FORMAT.copy()
        code = 200
        houses_ids = list(map(int, list(self.repository.values_list('id'))))
        if kwargs['pk'] not in houses_ids:
            resp['status'] = 'error'
            resp['message'] = 'No house with such id'
            code = 404
            return Response(data=resp, status=code)
        if not request.user.is_authenticated:
            resp['status'] = 'error'
            resp['message'] = 'Unauthorized'
            code = 401
            return Response(data=resp, status=code)
        obj = self.repository.filter(id=kwargs['pk'])[0]


        if request.user != obj.owner and request.user.type != 'admin':
            resp['status'] = 'error'
            resp['message'] = 'Not a house owner'
            code = 403
            return Response(data=resp, status=code)

        obj.delete()

        return Response(data=resp, status=code)

    @swagger_auto_schema(operation_summary='Edit a house',
                         operation_description="Edit a house",
                         responses={
                             '200': openapi.Response('Success editing an object', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_INTEGER, description='data')
                                 }, description='Success editing an object')),
                             '404': openapi.Response('No house with such id', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_INTEGER, description='data')
                                 }, description='No house with such id')),
                             '401': openapi.Response('Unauthorized', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_INTEGER, description='data')
                                 }, description='Unauthorized')),
                             '403': openapi.Response('Not the owner of the house', schema=openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_INTEGER, description='data')
                                 }, description='Not the owner of the house'))
                         },
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             properties={
                                 'name': openapi.Schema(type='string'),
                                 'desc': openapi.Schema(type='string', description='`House description'),
                                 'city_id': openapi.Schema(type='integer', description='House city id'),
                                 'guests_amount': openapi.Schema(type='integer',
                                                                 description='Maximum amount of guests'),
                                 'beds_amount': openapi.Schema(type='integer', description='Amount of beds'),
                                 'address': openapi.Schema(type='string', description='House address'),
                                 'rules': openapi.Schema(type='string', description='House rules'),
                                 'bathroom_amount': openapi.Schema(type='integer', description='Bathroom amount'),
                                 # 'facility': openapi.Schema(type=openapi.TYPE_STRING, description='House facilities'),
                                 # 'photoes': openapi.Schema(type=openapi.TYPE_FILE, description='House photoes')
                             },
                         ),
                         )
    def patch(self, request, *args, **kwargs):

        resp = RESPONSE_FORMAT.copy()
        code = 200
        houses_ids = list(map(int, list(self.repository.values_list('id', flat=True))))

        if kwargs['pk'] not in houses_ids:
            resp['status'] = 'error'
            resp['message'] = 'No house with such id'
            code = 400
            return Response(data=resp, status=code)

        if not request.user.is_authenticated:
            resp['status'] = 'error'
            resp['message'] = 'Unauthorized'
            code = 401
            return Response(data=resp, status=code)

        serialized = HouseUpdateSerializer(data=request.data)

        if not serialized.is_valid():
            resp['status'] = 'error'
            resp['message'] = 'Incorrect fields'
            code = 400
            return Response(data=resp, status=code)

        obj = self.repository.filter(id=kwargs['pk'])[0]


        if request.user != obj.owner and request.user.type != 'admin':
            resp['status'] = 'error'
            resp['message'] = 'Unauthorized'
            code = 403
            return Response(data=resp, status=code)

        self.repository.update(kwargs['pk'], serialized.data)
        return Response(data=resp, status=code)



class HouseEditView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    repository = HousesRepository()
    def delete(self, request, *args, **kwargs):
        resp = RESPONSE_FORMAT.copy()
        code = 200
        houses_ids = list(map(int, list(self.repository.values_list('id', flat=True))))
        if kwargs['pk'] not in houses_ids:
            resp['status'] = 'error'
            resp['message'] = 'No house with such id'
            code = 404
            return Response(data=resp, status=code)

        self.repository.delete(kwargs['pk'])

        return Response(data=resp, status=code)

    @swagger_auto_schema(operation_summary='Edit a house', methods=['PUT'],
                         operation_description="PUT /house/{id}/",
                         responses={
                             '200': openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_INTEGER, description='data')
                                 }, description='Success editing an object'),
                             '404': openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'status': openapi.Schema(type=openapi.TYPE_STRING, description='status_code'),
                                     'message': openapi.Schema(type=openapi.TYPE_STRING, description='message'),
                                     'data': openapi.Schema(type=openapi.TYPE_INTEGER, description='data')
                                 }, description='No house with such id')
                         },
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             properties={
                                 'name': openapi.Schema(type='string'),
                                 'desc': openapi.Schema(type='string', description='`House description'),
                                 'city_id': openapi.Schema(type='integer', description='House city id'),
                                 'guests_amount': openapi.Schema(type='integer',
                                                                 description='Maximum amount of guests'),
                                 'beds_amount': openapi.Schema(type='integer', description='Amount of beds'),
                                 'address': openapi.Schema(type='string', description='House address'),
                                 'rules': openapi.Schema(type='string', description='House rules'),
                                 'bathroom_amount': openapi.Schema(type='integer', description='Bathroom amount'),
                                 # 'facility': openapi.Schema(type=openapi.TYPE_STRING, description='House facilities'),
                                 # 'photoes': openapi.Schema(type=openapi.TYPE_FILE, description='House photoes')
                             },
                         ),
                         )
    @api_view(['PUT'])
    def put(self, request, *args, **kwargs):
        resp = RESPONSE_FORMAT.copy()
        code = 200
        houses_ids = list(map(int, list(self.repository.values_list('id', flat=True))))

        if kwargs['pk'] not in houses_ids:
            resp['status'] = 'error'
            resp['message'] = 'No house with such id'
            code = 400
            return Response(data=resp, status=code)

        serialized = HouseUpdateSerializer(data=request.data)

        if not serialized.is_valid():
            resp['status'] = 'error'
            resp['message'] = 'Incorrect fields'
            code = 400
            return Response(data=resp, status=code)


        self.repository.update(kwargs['pk'], serialized.data)
        return Response(data=resp, status=code)
