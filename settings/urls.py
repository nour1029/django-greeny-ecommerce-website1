from django.urls import path
from .views import contact_us

app_name = 'settings'



urlpatterns = [
    path('contact-us/', contact_us, name='contact_us'),
]
