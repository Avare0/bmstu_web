from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Countries(models.Model):
    name = models.CharField('Нахвание', max_length=50)


class Cities(models.Model):
    name = models.CharField('Название', max_length=50)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, verbose_name='Страна', blank=True, null=True,
                                related_name='cities_countries')

    def __str__(self):
        return self.name
SEXES = (
    ('m', 'Мужской'),
    ('f', 'Женский')
)
TYPES = (
    ('guest', 'Гость'),
    ('owner', 'Собственник')
)
class User(AbstractUser):
    sex = models.CharField(max_length=1, choices=SEXES)
    city = models.ForeignKey(Cities, on_delete=models.SET_DEFAULT, default=1)
    type = models.CharField(max_length=7, choices=TYPES, default='admin')
    photo = models.ImageField(upload_to='avatars/')


class Houses(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', blank=True, null=True)
    name = models.CharField('Название', max_length=50)
    desc = models.TextField('Описание', default='')
    city = models.ForeignKey(Cities, on_delete=models.SET_DEFAULT, default='', verbose_name='Город', null=True)
    guests_amount = models.IntegerField('Кол-во гостей', default='')
    beds_amount = models.IntegerField('Кол-во кроватей', default='')
    address = models.CharField('Адрес', max_length=100, default='')
    rules = models.TextField('Правила', default='Владелец не указал особых правил проживания')
    bathrooms_amount = models.IntegerField('Кол-во душей', default='')

    def __str__(self):
        return self.name

def nameFile(instance, filename):
    return '/'.join(['house_photos', filename])
class House_photos(models.Model):
    house = models.ForeignKey(Houses, on_delete=models.CASCADE, null=True, related_name='house_photo')
    photo = models.ImageField(upload_to=nameFile, null=True)


class Testimonials(models.Model):
    house = models.ForeignKey(Houses, on_delete=models.CASCADE, verbose_name='Дом', blank=True, null=True,
                              related_name='testimonials_house')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    text = models.TextField('Отзыв')
    date = models.DateField(auto_now=True, null=True)


class Orders(models.Model):
    house = models.ForeignKey(Houses, on_delete=models.CASCADE, verbose_name='Дом', blank=True, null=True,
                              related_name='orders_house')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True, )
    date_from = models.DateField('Дата начала', )
    date_till = models.DateField('Дата окончания')
    date = models.DateField('Дата бронирования', auto_now=True)
    guests_amount = models.IntegerField('Кол-во гостей', null=True)

class Facilities(models.Model):
    name = models.CharField('Name', max_length=50)
    file = models.FileField(default='1.jpg')

class House_Facilities(models.Model):
    house = models.ForeignKey(Houses, on_delete=models.CASCADE, verbose_name='Дом', related_name='house_facilities')
    facility = models.ForeignKey(Facilities, on_delete=models.CASCADE)
#
# class Messages(models.Model):
#     from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user_message')
#     to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user_message')
#     message = models.TextField()
#     date = models.DateTimeField(auto_now=True)



