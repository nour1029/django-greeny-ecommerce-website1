from itertools import product
from unicodedata import category
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


FLAG_TYPE = (
    ('New', 'New'),
    ('Featured', 'Featured')
)


class Product(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    sku = models.IntegerField(_("SKU"))
    brand = models.ForeignKey("Brand", verbose_name=_(
        "Brand"), on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField(_("Price"))
    desc = models.TextField(_("Description"), max_length=10000)
    tags = ''
    flag = models.CharField(_("Flag"), choices=FLAG_TYPE, max_length=15)
    category = models.ForeignKey("Category", verbose_name=_(
        "Category"), related_name='product_brand', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, verbose_name=_(
        "Product"), related_name='product_image', on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to='product/')

    def __str__(self):
        return str(self.product)


class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    image = models.ImageField(_("Image"), upload_to='category')

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, verbose_name=_(
        "Product"), related_name='product_review', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, verbose_name=_(
        "User"), related_name='review_author', on_delete=models.SET_NULL, null=True)
    review = models.TextField(_("Review"), max_length=500)
    rate = models.IntegerField(_("Rate"), validators=[
                               MaxValueValidator(5), MinValueValidator(0)])
    created_at = models.DateTimeField(_("Created at"), default=timezone.now)

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'
