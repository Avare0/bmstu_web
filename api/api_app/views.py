from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import *
from rest_framework.response import Response
from .permissions import *
from .serializers import *
from .models import *
from .forms import HouseForm

from datetime import datetime
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db.models import Q
from rest_framework.decorators import api_view
# from drf_yasg.openapi import *

RESPONSE_FORMAT = {
    'status': 'success',
    'data': None,
    'message': None
}
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

class HousesView(APIView):
    queryset = Houses.objects.all()
    serializer_class = HousesSerializer

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
                         )
    def get(self, request, *args, **kwargs):
        objects = Houses.objects.all()
        serialized = HousesSerializer(objects, many=True)
        resp = RESPONSE_FORMAT.copy()
        code = 200
        resp['data'] = serialized.data
        return Response(data=resp, status=code)


class UserHousesView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    @swagger_auto_schema(operation_summary='Get list of user houses',
                         operation_description='Get list of user houses',
                         responses={
                             '200': openapi.Response('List of user houses', schema=openapi.Schema(
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
                                                            }))
                                 }, description='List of user houses')),
                             '401': openapi.Response('Unauthorized', schema=openapi.Schema(type='object', properties={
                                 'detail': openapi.Schema(type='string')
                             }, description='User unauthorized')),
                         },
                         )
    def get(self, request):
        objects = Houses.objects.filter(owner=request.user)
        objects = HousesSerializer(objects, many=True).data
        return Response(data=objects, status=200)


class HouseView(APIView):

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
        house = Houses.objects.filter(id=self.kwargs['pk'])

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
        houses_ids = list(map(int, list(Houses.objects.values_list('id', flat=True))))
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
        obj = Houses.objects.filter(id=kwargs['pk'])

        if request.user != obj.owner:
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
        houses_ids = list(map(int, list(Houses.objects.values_list('id', flat=True))))

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

        obj = Houses.objects.filter(id=kwargs['pk'])


        if request.user != obj.owner:
            resp['status'] = 'error'
            resp['message'] = 'Unauthorized'
            code = 403
            return Response(data=resp, status=code)

        Houses.objects.filter(id=kwargs['pk']).update(**serialized.data)
        return Response(data=resp, status=code)

class HouseEditView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def delete(self, request, *args, **kwargs):
        resp = RESPONSE_FORMAT.copy()
        code = 200
        houses_ids = list(map(int, list(Houses.objects.values_list('id', flat=True))))
        if kwargs['pk'] not in houses_ids:
            resp['status'] = 'error'
            resp['message'] = 'No house with such id'
            code = 404
            return Response(data=resp, status=code)

        Houses.objects.filter(id=kwargs['pk']).delete()

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
        houses_ids = list(map(int, list(Houses.objects.values_list('id', flat=True))))

        if kwargs['pk'] not in houses_ids:
            resp['status'] = 'error'
            resp['message'] = 'No house with such id'
            code = 400
            return Response(data=resp, status=code)

        serialized = HouseUpdateSerializer(data=request.data)

        if not serialized.is_valid():
            print(serialized.errors)
            resp['status'] = 'error'
            resp['message'] = 'Incorrect fields'
            code = 400
            return Response(data=resp, status=code)

        obj = Houses.objects.filter(id=kwargs['pk'])

        Houses.objects.filter(id=kwargs['pk']).update(**serialized.data)
        return Response(data=resp, status=code)


class HouseCreateView(APIView):
    permission_classes = [IsAuthenticated]
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

        request.data.pop('facility')
        request.data.pop('photo')

        form = HouseForm(request.data)

        availiable_facilities = set(Facilities.objects.values_list('id', flat=True).distinct('id'))

        if len(availiable_facilities.intersection(set(facilities))) < len(facilities):
            resp['status'] = 'error'
            resp['message'] = 'Invalid facility ids'
            code = 400
            return Response(data=resp, status=code)

        if not form.is_valid():
            resp['status'] = 'error'
            resp['message'] = 'Invalid data in house infromation'
            code = 400
            return Response(data=resp, status=code)

        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()

        for id in facilities:
            House_Facilities.objects.create(
                house_id=obj.id,
                facility_id=id
            )
        for photo in photoes:
            House_photos.objects.create(
                house_id=obj.id,
                photo=photo
            )

        return Response(data=resp, status=code)


class CitiesView(APIView):
    response = openapi.Response('List of all cities', CitiesSerializer)

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
        cities = Cities.objects.all()
        cities = CitiesSerializer(cities, many=True).data

        resp['data'] = cities

        return Response(data=resp, status=code)


class TestimonialCreateView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(operation_summary='Create new order',
                         operation_description='Create order for a special house',
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
                                 'house_id': openapi.Schema(type='integer', description='house id'),
                             },
                         )
                         )
    def post(self, request):
        resp = RESPONSE_FORMAT.copy()
        code = 200

        if int(request.data['house_id']) not in list(map(int, list(Houses.objects.values_list('id', flat=True)))):
            resp['status'] = 'error'
            resp['message'] = 'No house with such id'
            code = 400
            return Response(data=resp, status=code)

        Testimonials.objects.create(
            house_id=int(request.data['house_id']),
            user=request.user,
            text=request.data['text']
        )

        return Response(data=resp, status=code)


class OrderCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def check_availiable_date(self, dt_from, dt_till):
        orders = Orders.objects.raw(
            f"""
            select * from api_app_orders
            where '{dt_from}'::date between date_from and date_till
            or '{dt_till}'::date between date_from and date_till
            or '{dt_from}'::date < date_from and date_till < '{dt_till}'::date
            """
        )
        return len(orders) == 0 and dt_from <= dt_till

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

        if int(request.data['house_id']) not in list(map(int, list(Houses.objects.values_list('id', flat=True)))):
            resp['status'] = 'error'
            resp['message'] = 'No house with such id'
            code = 400
            return Response(data=resp, status=code)

        house = Houses.objects.filter(id=int(request.data['house_id']))[0]

        if house.guests_amount < int(request.data['guests_amount']):
            resp['status'] = 'error'
            resp['message'] = 'Amount of guests is more than maximum amount'
            code = 400
            return Response(data=resp, status=code)



        if self.check_availiable_date(date_from, date_till):
            Orders.objects.create(
                house_id=int(request.data['house_id']),
                user=request.user,
                date_from=request.data['date_from'],
                date_till=request.data['date_till'],
                guests_amount=int(request.data['guests_amount'][0])
            )
        else:
            resp['status'] = 'error'
            resp['message'] = 'These dates are unavailable'
            code = 400
            return Response(data=resp, status=code)
        return Response(data=resp, status=code)


class UserRegisterView(APIView):

    @swagger_auto_schema(operation_summary='Create new order',
                         operation_description='Create order for a special house',
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
                                'photo': openapi.Schema(type='file', description='photo')
                             },
                         )
                         )
    def post(self, request):
        resp = RESPONSE_FORMAT.copy()
        code = 200
        serialized = UserSerializer2(data=request.data)
        if serialized.is_valid():
            user = serialized.save()
            if user:
                return Response(data=resp, status=code)
        else:
            resp['status'] = 'error'
            resp['message'] = serialized.errors
            code = 400
            return Response(data=resp, status=code)

class MyTokenObtainPairView(TokenObtainPairView):

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

    @swagger_auto_schema(operation_summary='Get JWT tokens',
                         operation_description='Get JWT tokens',
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