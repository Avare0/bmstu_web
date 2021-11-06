from django.contrib import admin
from .models import *
# Register your models here.
myModels = [User, Houses, House_photos, House_Facilities, Orders, Testimonials, Cities, Countries, ]  # iterable list
admin.site.register(myModels)