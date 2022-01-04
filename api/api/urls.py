"""api URL Configuration

The `urlpatterns` list routes URLs to components. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function components
    1. Add an import:  from my_app import components
    2. Add a URL to urlpatterns:  path('', components.home, name='home')
Class-based components
    1. Add an import:  from other_app.components import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api_app.urls')),
 ]
