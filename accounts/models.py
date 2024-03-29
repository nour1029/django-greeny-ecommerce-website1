from django.db import models
from django.contrib.auth.models import User
from settings.models import Country, City
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Product

from utils.code_generator import generate_code
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_(
        "User"), related_name='Profile', on_delete=models.CASCADE)
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    image = models.ImageField(
        _("Image"), upload_to='profile/', null=True, blank=True)
    code = models.CharField(_("Code"), max_length=8, default=generate_code)
    code_used = models.BooleanField(default=False)
    favorites = models.ManyToManyField(Product, verbose_name=_("Favorites"), related_name='favorites_product', blank=True)

    def get_favorites_count(self):
        favorites_count = self.favorites.count()
        return favorites_count

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


DATA_TYPE = (
    ('Home', 'Home'),
    ('Office', 'Office'),
    ('Bussiness', 'Bussiness'),
    ('Others', 'Others'),
)


class UserPhoneNumber(models.Model):
    user = models.ForeignKey(User, verbose_name=_(
        "User"), related_name='UserPhone', on_delete=models.CASCADE)
    phone_number = models.CharField(_("Phone Number"), max_length=15)
    type = models.CharField(_("Type"), max_length=10, choices=DATA_TYPE)
    active = models.BooleanField(_("Active"), default=False)

    def __str__(self):
        return f"{self.user.username} - {self.type}"


class UserAdress(models.Model):
    user = models.ForeignKey(User, verbose_name=_(
        "User"), related_name='UserAdress', on_delete=models.CASCADE)
    type = models.CharField(_("Type"), max_length=10, choices=DATA_TYPE)
    country = models.ForeignKey(Country, verbose_name=_(
        "Country"), related_name='user_country', on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, verbose_name=_(
        "City"), related_name='user_city', on_delete=models.SET_NULL, null=True)
    state = models.CharField(_("State"), max_length=50)
    region = models.CharField(_("Region"), max_length=50)
    street = models.CharField(_("Street"), max_length=50)
    notes = models.TextField(_("Notes"), max_length=50, null=True, blank=True)
    active = models.BooleanField(_("Active"), default=False)

    def __str__(self):
        return f"{self.user.username} - {self.type}"
