from django.test import TestCase
from ..repositories.FacilitiesRepository import *
from django.core.files import File as DjangoFile
from ..repositories.UsersRepository import *
from ..repositories.OrdersRepository import *
from ..repositories.TestimonialsRepository import *
from ..repositories.CitiesRepository import *
from ..repositories.HousesRepository import *
from .testimonial_builder import TestimonialBuilder
from datetime import date


class CitiesRepositoryTest(TestCase):

    def setUp(self):
        self.rep = CitiesRepository()

        self.moscow = self.rep.create(name='Moscow')
        self.paris = self.rep.create(name='Paris')

    # def tearDown(self):
    #     # Очистка после каждого метода
    #     pass

    def test_get_city_by_name(self):
        city = self.rep.filter(name='Moscow')

        self.assertEqual(city[0].name, self.moscow.name)
        self.assertTrue(len(city) == 1)

    def test_get_city_by_name_fail(self):
        city = self.rep.filter(name='Moscow1')

        self.assertTrue(len(city) == 0)

    def test_update_object(self):
        city_upd = Cities(name='Beijing')
        self.rep.update(self.moscow.id, {'name': 'Beijing'})

        city = self.rep.filter(name='Beijing')

        self.assertEqual(city_upd.name, city[0].name)
        self.assertTrue(len(city) == 1)

    def test_get_all_cities(self):
        cities = self.rep.all()

        self.assertTrue(len(cities) == 2)
        self.assertTrue(cities[0].name, self.moscow.name)
        self.assertTrue(cities[1].name, self.paris.name)


class FacilitiesRepositoryTest(TestCase):
    def setUp(self):
        self.rep = FacilitiesRepository()

        self.img = DjangoFile(open('api_app/tests/conditioner.png', mode='rb'), name='file.png')

        self.f1 = self.rep.create(name='Facility1', file=self.img)
        self.f2 = self.rep.create(name='Facility2', file=self.img)

    # def tearDown(self):
    #     # Очистка после каждого метода
    #     pass

    def test_get_facility_by_name(self):
        facility = self.rep.filter(name='Facility1')

        self.assertEqual(facility[0].name, self.f1.name)
        self.assertTrue(len(facility) == 1)

    def test_get_facility_by_name_fail(self):
        facility = self.rep.filter(name='Facility143')

        self.assertTrue(len(facility) == 0)

    def test_update_object(self):
        facility_upd = Facilities(name='Facility3', file=self.img)

        self.rep.update(self.f1.id, {'name': 'Facility3'})

        facility = self.rep.filter(name='Facility3')

        self.assertEqual(facility_upd.name, facility[0].name)
        self.assertTrue(len(facility) == 1)

    def test_get_all_facility(self):
        facilities = self.rep.all()

        self.assertTrue(len(facilities) == 2)
        self.assertTrue(facilities[0].name, self.f1.name)
        self.assertTrue(facilities[1].name, self.f2.name)


class HouseRepositoryTest(TestCase):
    def setUp(self):
        self.rep = HousesRepository()
        self.city_rep = CitiesRepository()
        self.user_rep = UsersRepository()

        self.city = self.city_rep.create(name='Moscow')
        self.user1 = self.user_rep.create(username='123',
                                          first_name='Egor',
                                          last_name='Panafidin',
                                          city=self.city,
                                          type='guest',
                                          sex='m',
                                          password='123')
        self.user2 = self.user_rep.create(username='456',
                                          first_name='Egor',
                                          last_name='Panafidin',
                                          city=self.city,
                                          type='guest',
                                          sex='m',
                                          password='123')
        self.user3 = self.user_rep.create(username='45611',
                                          first_name='Egor',
                                          last_name='Panafidin',
                                          city=self.city,
                                          type='guest',
                                          sex='m',
                                          password='123')
        self.house1 = self.rep.create(name='123',
                                      desc='123',
                                      city=self.city,
                                      guests_amount=5,
                                      beds_amount=1,
                                      address='123',
                                      rules='123',
                                      bathrooms_amount=1,
                                      owner=self.user1)
        self.house2 = self.rep.create(name='123222',
                                      desc='123',
                                      city=self.city,
                                      guests_amount=5,
                                      beds_amount=3,
                                      address='123',
                                      rules='123',
                                      bathrooms_amount=1,
                                      owner=self.user1)
        self.house3 = self.rep.create(name='123444',
                                      desc='123',
                                      city=self.city,
                                      guests_amount=5,
                                      beds_amount=3,
                                      address='123',
                                      rules='123',
                                      bathrooms_amount=1,
                                      owner=self.user2)

    def test_get_owner_houses(self):
        res = self.rep.filter(owner=self.user2)

        self.assertTrue(len(res) == 1)
        self.assertEqual(self.house3, res[0])

    def test_get_owner_houses2(self):
        res = self.rep.filter(owner=self.user1)

        self.assertTrue(len(res) == 2)
        self.assertEqual(self.house1, res[0])
        self.assertEqual(self.house2, res[1])

    def test_get_owner_houses_fail(self):
        res = self.rep.filter(owner=self.user3)

        self.assertTrue(len(res) == 0)

    def test_get_house_by_id(self):
        res = self.rep.filter(id=self.house1.id)

        self.assertTrue(len(res) == 1)
        self.assertEqual(self.house1, res[0])

    def test_get_house_by_id_fail(self):
        res = self.rep.filter(id=9999999)

        self.assertTrue(len(res) == 0)

    def test_delete_house(self):
        self.rep.delete(self.house1.id)

        res = self.rep.filter(id=self.house1.id)

        self.assertTrue(len(res) == 0)


class OrdersRepositoryTest(TestCase):
    def setUp(self):
        self.rep = OrdersRepository()
        self.house_rep = HousesRepository()
        self.city_rep = CitiesRepository()

        self.city = self.city_rep.create(name='Moscow')

        self.house = self.house_rep.create(name='123',
                                           desc='123',
                                           city=self.city,
                                           guests_amount=5,
                                           beds_amount=1,
                                           address='123',
                                           rules='123',
                                           bathrooms_amount=1)
        self.house_fail = self.house_rep.create(name='123',
                                                desc='123',
                                                city=self.city,
                                                guests_amount=5,
                                                beds_amount=3,
                                                address='123',
                                                rules='123',
                                                bathrooms_amount=1)

        self.order1 = self.rep.create(house=self.house,
                                      guests_amount=12,
                                      date='2021-10-10',
                                      date_from='2021-10-11',
                                      date_till='2021-10-15')
        self.order2 = self.rep.create(house=self.house,
                                      guests_amount=12,
                                      date='2021-10-10',
                                      date_from='2021-10-18',
                                      date_till='2021-10-26')
        self.order3 = self.rep.create(guests_amount=12,
                                      date_from='2021-10-11',
                                      date_till='2021-10-15')

    def test_get_house_orders(self):
        res = self.rep.filter(house=self.house)

        self.assertTrue(len(res) == 2)
        self.assertEqual(res[0], self.order1)
        self.assertEqual(res[1], self.order2)

    def test_get_house_orders_fail(self):
        res = self.rep.filter(house=self.house_fail)

        self.assertTrue(len(res) == 0)

    def test_get_all_testimonials(self):
        res = self.rep.all()

        self.assertTrue(len(res) == 3)
        self.assertEqual(res[0], self.order1)
        self.assertEqual(res[1], self.order2)
        self.assertEqual(res[2], self.order3)

    def test_auto_date(self):
        self.assertEqual(self.order3.date.isoformat(), date.today().isoformat())

    def test_check_availiable_dates_fail(self):
        res = self.rep.check_availiable_date('2021-10-09', '2021-10-16', self.house.id)

        self.assertFalse(res)

    def test_check_availiable_dates(self):
        res = self.rep.check_availiable_date('2021-09-09', '2021-09-16', self.house.id)

        self.assertTrue(res)

    def test_check_availiable_dates_fail(self):
        res = self.rep.check_availiable_date('2021-10-12', '2021-10-14', self.house.id)

        self.assertFalse(res)


class TestimonialsRepositoryTest(TestCase):
    def setUp(self):
        self.rep = TestimonialsRepository()
        self.house_rep = HousesRepository()
        self.city_rep = CitiesRepository()

        self.city = self.city_rep.create(name='Moscow')

        self.house = self.house_rep.create(name='123',
                                           desc='123',
                                           city=self.city,
                                           guests_amount=5,
                                           beds_amount=1,
                                           address='123',
                                           rules='123',
                                           bathrooms_amount=1)
        self.house_fail = self.house_rep.create(name='123',
                                                desc='123',
                                                city=self.city,
                                                guests_amount=5,
                                                beds_amount=3,
                                                address='123',
                                                rules='123',
                                                bathrooms_amount=1)

        self.testimonial = TestimonialBuilder().with_text('123') \
            .with_date('2021-10-10').with_house(self.house.id).build()

        # self.testimonial = self.rep.create(house=self.house,
        #                                    text='123',
        #                                    date='2021-10-10')
        self.testimonial2 = self.rep.create(house=self.house,
                                            text='1232',
                                            date='2021-10-11')
        self.testimonial3 = self.rep.create(
            text='1232',
            date='2021-10-11')

    def test_get_house_testimonials(self):
        res = self.rep.filter(house=self.house)

        self.assertTrue(len(res) == 2)
        self.assertEqual(res[0], self.testimonial)
        self.assertEqual(res[1], self.testimonial2)

    def test_get_house_testimonials_fail(self):
        res = self.rep.filter(house=self.house_fail)

        self.assertTrue(len(res) == 0)

    def test_get_all_testimonials(self):
        res = self.rep.all()

        self.assertTrue(len(res) == 3)
        self.assertEqual(res[0], self.testimonial)
        self.assertEqual(res[1], self.testimonial2)
        self.assertEqual(res[2], self.testimonial3)
