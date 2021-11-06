from django.urls import include, path
from rest_framework import routers
from django.conf.urls import url
from . import views
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
    # path('', include(router.urls)),
    # path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('house/<int:pk>', views.HouseView.as_view(), name='house_details'),
    path('testimonial', views.TestimonialCreateView.as_view(), name='testimonial_create'),

    path('order', views.OrderCreateView.as_view(), name='order_create'),

    path('house/list', views.HousesView.as_view(), name='house_list'),
    path('house/create', views.HouseCreateView.as_view(), name='house_create'),

    path('house/list/my', views.UserHousesView.as_view(), name='user_houses'),

    path('cities', views.CitiesView.as_view(), name='cities'),


    path('token', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', views.MyTokenRefreshView.as_view(), name='token_refresh'),

    path('register', views.UserRegisterView.as_view(), name='user_register'),
]