from django.contrib import admin

# Register your models here.
from .models import Profile, UserAdress, UserPhoneNumber


class UserPhoneNumberAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active']

class UserAdressAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active', 'street']


admin.site.register(Profile)
admin.site.register(UserAdress, UserAdressAdmin)
admin.site.register(UserPhoneNumber, UserPhoneNumberAdmin)
