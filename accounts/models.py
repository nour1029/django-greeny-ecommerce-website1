from django.db import models
from django.contrib.auth.models import User
from settings.models import Country, City
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_(
        "User"), related_name='Profile', on_delete=models.CASCADE)
    image = models.ImageField(
        _("Image"), upload_to='profile/', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


DATA_TYPE = (
    ('Home', 'Home'),
    ('Office', 'Office'),
    ('Bussines', 'Bussines'),
    ('Others', 'Others'),
)


class UserPhoneNumber(models.Model):
    user = models.ForeignKey(User, verbose_name=_(
        "User"), related_name='UserPhone', on_delete=models.CASCADE)
    phone_number = models.CharField(_("Phone Number"), max_length=15)
    type = models.CharField(_("Type"), max_length=10, choices=DATA_TYPE)

    def __str__(self):
        return f"{self.user.username} - {self.type}"


class UserAdress(models.Model):
    user = models.OneToOneField(User, verbose_name=_(
        "User"), related_name='UserAdress', on_delete=models.CASCADE)
    type = models.CharField(_("Type"), max_length=10, choices=DATA_TYPE)
    country = models.ForeignKey(Country, verbose_name=_(
        "Country"), related_name='user_country', on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, verbose_name=_(
        "City"), related_name='user_city', on_delete=models.SET_NULL, null=True)
    state = models.CharField(_("State"), max_length=50)
    region = models.CharField(_("Region"), max_length=50)
    street = models.CharField(_("Street"), max_length=50)
    notes = models.CharField(_("Notes"), max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.type}"
