from importlib.abc import Traversable
from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class City(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    country = models.ForeignKey("Country", verbose_name=_(
        "Country"), related_name='country_city', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    logo = models.ImageField(_("Logo"), upload_to='company/')
    about = models.CharField(_("About"), max_length=3000)
    fb_link = models.URLField(_("Facebook Link"), null=True, blank=True)
    tw_link = models.URLField(_("Twitter Link"), null=True, blank=True)
    ins_link = models.URLField(_("Instagram Link"), null=True, blank=True)
    email = models.EmailField(_("Email"), max_length=30)
    phone_number = models.CharField(_("Phone Number"), max_length=20)
    address = models.CharField(_("Address"), max_length=100)
    address_googlemaps = models.URLField(_("Google Maps Adress URL"), max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name
