from django.urls import include, path
from rest_framework import routers
from django.conf.urls import url
from . import views
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import *


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [

    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('houses/<int:pk>', HouseView.as_view(), name='house_details'),
    path('houses/<int:pk>/testimonials', TestimonialCreateView.as_view(), name='testimonial_create'),

    path('orders', OrdersView.as_view(), name='order_create'),

    path('houses', HousesView.as_view(), name='house_list'),

    path('cities', CitiesView.as_view(), name='cities'),

    path('users/token',MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/refresh', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('users', UsersView.as_view(), name='user_register'),
]