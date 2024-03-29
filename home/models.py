from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class Banner(models.Model):
    title_en = models.CharField(_("English Title"), max_length=50)
    title_ar = models.CharField(_("Arabic Title"), max_length=50)
    sub_title = models.CharField(_("Sub Title"), max_length=150)
    image = models.ImageField(_("Image"), upload_to='banner/')
    active = models.BooleanField(_("Active"), default=False)

    def __str__(self):
        return self.title_en
