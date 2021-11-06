from rest_framework import serializers

from .models import *

class CountriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Countries
        fields = ('name',)

class CitiesSerializer(serializers.HyperlinkedModelSerializer):
    country = CountriesSerializer(read_only=True)
    class Meta:
        model = Cities
        fields = ('name', 'country',)

class HouseUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Houses
        # fields = '__all__'
        exclude = ('owner',)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'photo',)

class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password',
                  'username', 'email', 'sex', 'type', 'photo', 'city')
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        # if password is not None:
        instance.set_password(password)
        instance.save()
        return instance
class House_photosSerializer(serializers.ModelSerializer):
    class Meta:
        model = House_photos
        fields = ('photo', )

class TestimonialsSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Testimonials
        fields = ('user', 'text', 'date')

class OrdersSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Orders
        fields = '__all__'

class FacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = '__all__'


class House_FacilitiesSerializer(serializers.ModelSerializer):
    facility = FacilitiesSerializer()
    class Meta:
        model = House_Facilities
        fields = '__all__'

class HousesSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    city = CitiesSerializer()
    house_photo = House_photosSerializer(many=True)
    testimonials_house = TestimonialsSerializer(many=True)
    orders_house = OrdersSerializer(many=True)
    house_facilities = House_FacilitiesSerializer(many=True)
    class Meta:
        model = Houses
        fields = '__all__'



class TestimonialsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'

class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class FacilitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Facilities
        fields = '__all__'

class House_FacilitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = House_Facilities
        fields = '__all__'
#
# class MessagesSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Messages
#         fields = '__all__'