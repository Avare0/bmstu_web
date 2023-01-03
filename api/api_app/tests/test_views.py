from django.test import TestCase
from mock import patch

from ..repositories.CitiesRepository import *
from django.urls import reverse

import pickle
import json
from ..repositories.HousesRepository import *
from ..repositories.OrdersRepository import *
from ..repositories.UsersRepository import *
from ..repositories.TestimonialsRepository import *
from ..repositories.FacilitiesRepository import *
from ..repositories.HouseFaciltiiesRepository import *
class CitiesViewTest(TestCase):

    def test_response(self):
        data = open("api_app/tests/queryset_dumps/cities.dump", "rb").read()
        cities = pickle.loads(data)
        with patch.object(CitiesRepository, 'all', return_value=cities):
            url = reverse('cities')
            response = self.client.get(url)
            content = response.content.decode()
            js = json.loads(content)

            self.assertEqual(js['status'], 'success')
            self.assertEqual(js['data'], [{"name": "Moscow", "country": None, "id": 9},
                                          {"name": "Saint-Petersburg", "country": None, "id": 10}])
            self.assertEqual(js['message'], None)

    def test_response_empty(self):
        data = open("api_app/tests/queryset_dumps/cities_empty.dump", "rb").read()
        cities = pickle.loads(data)
        with patch.object(CitiesRepository, 'all', return_value=cities):
            url = reverse('cities')
            response = self.client.get(url)
            content = response.content.decode()
            js = json.loads(content)


            self.assertEqual(js['status'], 'success')
            self.assertEqual(js['data'], [])
            self.assertEqual(js['message'], None)

class OrdersViewTest(TestCase):
    def setUp(self):
        self.cities_rep = CitiesRepository()
        city = self.cities_rep.create(name='Moscow')
        self.user_rep = UsersRepository()
        self.user1 = self.user_rep.create(username='123',
                                          first_name='Egor',
                                          last_name='Panafidin',
                                          type='guest',
                                          city=city,
                                          sex='m',
                                          password='123')
        self.client.login(username='123', password='123')

    def test_create_response_fail(self):
        data = open("api_app/tests/queryset_dumps/house_list.dump", "rb").read()
        data = pickle.loads(data)
        with patch.object(HousesRepository, 'values_list', return_value=data):
            url = reverse('order_create')
            response = self.client.post(url, data={'house_id': 2222, 'date_from': '2021-10-11', 'date_till': '2021-10-15'})
            content = response.content.decode()
            js = json.loads(content)

            self.assertEqual(js['status'], 'error')
            self.assertEqual(js['data'], None)
            self.assertEqual(js['message'], 'No house with such id')
            self.assertEqual(response.status_code, 400)
    def test_create_response_fail2(self):
        data = open("api_app/tests/queryset_dumps/house_list.dump", "rb").read()
        data = pickle.loads(data)
        with patch.object(HousesRepository, 'values_list', return_value=data):
            url = reverse('order_create')
            response = self.client.post(url, data={'house_id': 2222, 'date_from': '2021-a0-11', 'date_till': '2021-10-15'})
            content = response.content.decode()
            js = json.loads(content)

            self.assertEqual(js['status'], 'error')
            self.assertEqual(js['data'], None)
            self.assertEqual(js['message'], 'Incorrect dates, they should be in format yyyy-mm-dd')
            self.assertEqual(response.status_code, 400)

    def test_create_response_fail3(self):
        data = open("api_app/tests/queryset_dumps/house_list.dump", "rb").read()
        data = pickle.loads(data)
        with patch.object(HousesRepository, 'values_list', return_value=data):
            url = reverse('order_create')
            response = self.client.post(url, data={'house_id': 2222, 'date_from': '2021-10-11', 'date_till': '2021-15-123'})
            content = response.content.decode()
            js = json.loads(content)

            self.assertEqual(js['status'], 'error')
            self.assertEqual(js['data'], None)
            self.assertEqual(js['message'], 'Incorrect dates, they should be in format yyyy-mm-dd')
            self.assertEqual(response.status_code, 400)

    def test_create_response_success(self):
        data = open("api_app/tests/queryset_dumps/house_list.dump", "rb").read()
        data1 = pickle.loads(data)
        data = open("api_app/tests/queryset_dumps/houses.dump", "rb").read()
        data2 = pickle.loads(data)
        with patch.object(HousesRepository, 'values_list', return_value=data1):
            with patch.object(HousesRepository, 'filter', return_value=data2):
                with patch.object(OrdersRepository, 'create', return_value='success'):
                    url = reverse('order_create')
                    response = self.client.post(url, data={'house_id': 9, 'date_from': '2021-10-11', 'date_till': '2021-10-15',
                                                           'guests_amount': 2})
                    content = response.content.decode()
                    js = json.loads(content)

                    self.assertEqual(js['message'], None)
                    self.assertEqual(js['status'], 'success')
                    self.assertEqual(js['data'], None)

                    self.assertEqual(response.status_code, 200)
    def test_create_response_fail4(self):
        data = open("api_app/tests/queryset_dumps/house_list.dump", "rb").read()
        data1 = pickle.loads(data)
        data = open("api_app/tests/queryset_dumps/houses.dump", "rb").read()
        data2 = pickle.loads(data)
        with patch.object(HousesRepository, 'values_list', return_value=data1):
            with patch.object(HousesRepository, 'filter', return_value=data2):
                url = reverse('order_create')
                response = self.client.post(url, data={'house_id': 9, 'date_from': '2021-10-11', 'date_till': '2021-10-12', 'guests_amount': 10})
                content = response.content.decode()
                js = json.loads(content)

                self.assertEqual(js['status'], 'error')
                self.assertEqual(js['data'], None)
                self.assertEqual(js['message'], 'Amount of guests is more than maximum amount')
                self.assertEqual(response.status_code, 400)

    def test_create_response_fail6(self):
        data = open("api_app/tests/queryset_dumps/house_list.dump", "rb").read()
        data1 = pickle.loads(data)
        data = open("api_app/tests/queryset_dumps/houses.dump", "rb").read()
        data2 = pickle.loads(data)
        with patch.object(HousesRepository, 'values_list', return_value=data1):
            with patch.object(HousesRepository, 'filter', return_value=data2):
                url = reverse('order_create')
                response = self.client.post(url,
                                            data={'house_id': 9, 'date_from': '2021-10-11', 'date_till': '2021-10-10',
                                                  'guests_amount': 1})
                content = response.content.decode()
                js = json.loads(content)

                self.assertEqual(js['status'], 'error')
                self.assertEqual(js['data'], None)
                self.assertEqual(js['message'],  'These dates are unavailable')
                self.assertEqual(response.status_code, 400)

    def test_get_orders_fail1(self):
        url = reverse('order_create')
        response = self.client.get(url, {'user_id': self.user1.id + 1})
        content = response.content.decode()
        js = json.loads(content)

        self.assertEqual(js['status'], 'error')
        self.assertEqual(js['data'], None)
        self.assertEqual(js['message'], 'Only user with this id can access this')
        self.assertEqual(response.status_code, 403)
    def test_get_orders_fail2(self):
        url = reverse('order_create')
        response = self.client.get(url, {'blabla': self.user1.id + 1})
        content = response.content.decode()
        js = json.loads(content)

        self.assertEqual(js['status'], 'error')
        self.assertEqual(js['data'], None)
        self.assertEqual(js['message'], 'Incorrect query params or no params passed')
        self.assertEqual(response.status_code, 404)

class TestimonialsViewTest(TestCase):
    # def setUp(self):
    #     self.cities_rep = CitiesRepository()
    #     city = self.cities_rep.create(name='Moscow')
    #     self.user_rep = UsersRepository()
    #     self.user1 = self.user_rep.create(username='123',
    #                                       first_name='Egor',
    #                                       last_name='Panafidin',
    #                                       type='guest',
    #                                       city=city,
    #                                       sex='m',
    #                                       password='123')
    #     with open('api_app/tests/queryset_dumps/testimonials_empty.dump', 'wb') as f:
    #         pickle.dump(TestimonialsRepository().all(), f)
    #
    #     self.house = HousesRepository().create(name='123',
    #                                        desc='123',
    #                                        city=city,
    #                                        guests_amount=5,
    #                                        beds_amount=1,
    #                                        address='123',
    #                                        rules='123',
    #                                        bathrooms_amount=1,
    #                                  owner=self.user1)
    #     self.testimonial = TestimonialsRepository().create(house=self.house, user=self.user1, text='123')
    #     self.testimonial = TestimonialsRepository().create(house=self.house, user=self.user1, text='123123')
    #
    #     with open('api_app/tests/queryset_dumps/testimonials.dump', 'wb') as f:
    #         pickle.dump(TestimonialsRepository().all(), f)
    #
    #     # print(TestimonialsSerializer(TestimonialsRepository().filter(house_id=1), many=True).data)
    #     print(self.house.id)


    def test_create_response_fail(self):
        self.client.login(username='123', password='123')
        data = open("api_app/tests/queryset_dumps/house_list.dump", "rb").read()
        data = pickle.loads(data)
        with patch.object(HousesRepository, 'values_list', return_value=data):
            url = reverse('testimonial_create', args=[1])
            response = self.client.post(url, data={'pk': 2222})
            content = response.content.decode()
            js = json.loads(content)

            self.assertEqual(js['status'], 'error')
            self.assertEqual(js['data'], None)
            self.assertEqual(js['message'], 'No house with such id')
            self.assertEqual(response.status_code, 400)
    def test_create_response_fail1(self):
        data = open("api_app/tests/queryset_dumps/house_list.dump", "rb").read()
        data = pickle.loads(data)
        with patch.object(HousesRepository, 'values_list', return_value=data):
            url = reverse('testimonial_create', args=[9])
            response = self.client.post(url, data={'pk': 9})
            content = response.content.decode()
            js = json.loads(content)

            self.assertEqual(js['status'], 'error')
            self.assertEqual(js['data'], None)
            self.assertEqual(js['message'], 'Unauthorized')
            self.assertEqual(response.status_code, 401)

    def test_get_house_testimonials(self):
        data = open("api_app/tests/queryset_dumps/testimonials.dump", "rb").read()
        data = pickle.loads(data)
        with patch.object(TestimonialsRepository, 'filter', return_value=data):
            url = reverse('testimonial_create', args=[1])
            response = self.client.get(url)
            content = response.content.decode()
            js = json.loads(content)

            self.assertEqual(js['status'], 'success')
            self.assertEqual(js['data'], [{'id': 1, 'user': None, 'text': '123', 'date': '2022-01-06', 'house': 1}, {'id': 2, 'user': None, 'text': '123123', 'date': '2022-01-06', 'house': 1}])
            self.assertEqual(js['message'], None)
            self.assertEqual(response.status_code, 200)

    def test_get_house_testimonials1(self):
        data = open("api_app/tests/queryset_dumps/testimonials_empty.dump", "rb").read()
        data = pickle.loads(data)
        with patch.object(HousesRepository, 'filter', return_value=data):
            url = reverse('testimonial_create', args=[44])
            response = self.client.get(url)
            content = response.content.decode()
            js = json.loads(content)

            self.assertEqual(js['status'], 'success')
            self.assertEqual(js['data'], [])
            self.assertEqual(js['message'], None)
            self.assertEqual(response.status_code, 200)





class UsersViewTest(TestCase):
    # def setUp(self):
    #     self.cities_rep = CitiesRepository()
    #     city = self.cities_rep.create(name='Moscow')
    #     self.user_rep = UsersRepository()
    #     self.user1 = self.user_rep.create(username='123',
    #                                       first_name='Egor',
    #                                       last_name='Panafidin',
    #                                       type='guest',
    #                                       city=city,
    #                                       sex='m',
    #                                       password='123')
    #     with open('api_app/tests/queryset_dumps/user.dump', 'wb') as f:
    #         pickle.dump(UsersRepository().all(), f)
    #     with open('api_app/tests/queryset_dumps/user_empty.dump', 'wb') as f:
    #         pickle.dump(UsersRepository().filter(id=111111), f)
    #     print(self.user1.id)

    def test_get_by_user_id(self):
        data = open("api_app/tests/queryset_dumps/user.dump", "rb").read()
        data = pickle.loads(data)
        with patch.object(UsersRepository, 'filter', return_value=data):
            url = reverse('user_register')
            response = self.client.get(url, {'id': 11})
            content = response.content.decode()
            js = json.loads(content)

            self.assertEqual(js['status'], 'success')
            self.assertEqual(js['data'], {'id': 11, 'username': '123', 'first_name': 'Egor', 'last_name': 'Panafidin', 'email': '', 'sex': 'm', 'type': 'guest', 'photo': None, 'city': 19})
            self.assertEqual(js['message'], None)
            self.assertEqual(response.status_code, 200)


    def test_get_by_user_id_fail2(self):
        data = open("api_app/tests/queryset_dumps/user_empty.dump", "rb").read()
        data = pickle.loads(data)
        with patch.object(UsersRepository, 'filter', return_value=data):
            url = reverse('user_register')
            response = self.client.get(url, {'asdasd': 55})
            content = response.content.decode()
            js = json.loads(content)

            self.assertEqual(js['status'], 'error')
            self.assertEqual(js['data'], None)
            self.assertEqual(js['message'], 'No such method exists')
            self.assertEqual(response.status_code, 400)

class HouseViewTest(TestCase):
    def setUp(self):
        self.cities_rep = CitiesRepository()
        city = self.cities_rep.create(name='Moscow')
        self.user_rep = UsersRepository()
        self.user1 = self.user_rep.create(username='123',
                                          first_name='Egor',
                                          last_name='Panafidin',
                                          type='guest',
                                          city=city,
                                          sex='m',
                                          password='123')
        self.client.login(username='123', password='123')
    def test_get_all_houses2(self):
        data = open("api_app/tests/queryset_dumps/houses.dump", "rb").read()
        data = pickle.loads(data)
        with patch.object(HousesRepository, 'all', return_value=data):
            url = reverse('house_list')
            response = self.client.get(url)
            content = response.content.decode()
            js = json.loads(content)

            self.assertEqual(js['status'], 'success')
            self.assertEqual(js['data'], [{'id': 9, 'owner': None, 'city': None, 'house_photo': [], 'testimonials_house': [], 'orders_house': [], 'house_facilities': [], 'name': '123', 'desc': '123', 'guests_amount': 5, 'beds_amount': 1, 'address': '123', 'rules': '123', 'bathrooms_amount': 1}])
            self.assertEqual(js['message'], None)
            self.assertEqual(response.status_code, 200)

    def test_get_all_houses3(self):
        data = []
        with patch.object(HousesRepository, 'filter', return_value=data):
            url = reverse('house_list')
            response = self.client.get(url, {'user_id': 132123})
            content = response.content.decode()
            js = json.loads(content)

            self.assertEqual(js['status'], 'error')
            self.assertEqual(js['data'], None)
            self.assertEqual(js['message'], 'Only user with this id can access this')
            self.assertEqual(response.status_code, 403)

    def test_get_all_houses4(self):
        data = []
        with patch.object(HousesRepository, 'filter', return_value=data):
            url = reverse('house_list')
            response = self.client.get(url, {'user_id': self.user1.id})
            content = response.content.decode()
            js = json.loads(content)

            self.assertEqual(js['status'], 'error')
            self.assertEqual(js['data'], None)
            self.assertEqual(js['message'], 'Only user with this id can access this')
            self.assertEqual(response.status_code, 403)

    def test_create_house_fail1(self):
        with patch.object(FacilitiesRepository, 'values_list', return_value=[1,2,3]):
            url = reverse('house_list')
            response = self.client.post(url, dict(name=1,
                                                   desc='123',
                                                   guests_amount=5,
                                                   beds_amount=1,
                                                   address='123',
                                                   rules='123',
                                                   bathrooms_amount=1,
                                                         facility=[4,1,2]))
            content = response.content.decode()
            js = json.loads(content)

            self.assertEqual(js['status'], 'error')
            self.assertEqual(js['data'], None)
            self.assertEqual(js['message'], 'Invalid facility ids')
            self.assertEqual(response.status_code, 400)
    def test_create_house_fail2(self):
        with patch.object(FacilitiesRepository, 'values_list', return_value=[1,2,3]):
            url = reverse('house_list')
            response = self.client.post(url, dict(name='123',
                                                   desc='123',
                                                   guests_amount=5,
                                                   beds_amount='asd',
                                                   address='123',
                                                   rules='123',
                                                   bathrooms_amount=1,
                                                         facility=[1,2,3]))
            content = response.content.decode()
            js = json.loads(content)

            self.assertEqual(js['status'], 'error')
            self.assertEqual(js['data'], None)
            self.assertEqual(js['message'], 'Invalid data in house information')
            self.assertEqual(response.status_code, 400)

    def test_create_house_fail3(self):
        with patch.object(FacilitiesRepository, 'values_list', return_value=[1,2,3]):
            with patch.object(HousesFacilitiesRepository, 'create', return_value=None):
                url = reverse('house_list')
                response = self.client.post(url, dict(name='123',
                                                       desc='123',
                                                       guests_amount=5,
                                                       beds_amount=2,
                                                       address='123',
                                                       rules='123',
                                                       bathrooms_amount=1,
                                                             facility=[1,2,3]))
                content = response.content.decode()
                js = json.loads(content)

                self.assertEqual(js['status'], 'success')
                self.assertEqual(js['data'], None)
                self.assertEqual(js['message'], None)
                self.assertEqual(response.status_code, 200)