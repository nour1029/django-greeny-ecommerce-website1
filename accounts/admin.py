from django.contrib import admin

# Register your models here.
from .models import Profile, UserAdress, UserPhoneNumber


admin.site.register(Profile)
admin.site.register(UserAdress)
admin.site.register(UserPhoneNumber)
