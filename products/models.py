from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.db.models import Avg
from django.urls import reverse
# Create your models here.


FLAG_TYPE = (
    ('New', _('New')),
    ('Featured', _('Featured')),
)


class PollManager(models.Manager):
    def rate_avg(self, rate):
        rate = int(rate)
        rate_min = rate-0.5
        rate_max = rate+0.5
        return self.annotate(rate_avg=Avg('product_review__rate')).filter(rate_avg__gte=rate_min, rate_avg__lt=rate_max)

class Product(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    sku = models.IntegerField(_("SKU"))
    brand = models.ForeignKey("Brand", verbose_name=_(
        "Brand"), related_name='product_brand', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField(_("Price"))
    desc = models.TextField(_("Description"), max_length=10000)
    tags = TaggableManager(blank=True)
    flag = models.CharField(_("Flag"), choices=FLAG_TYPE, max_length=15)
    category = models.ForeignKey("Category", verbose_name=_(
        "Category"), related_name='product_category', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(_("Image"), upload_to='products/')
    video_url = models.URLField(_("Video URL"), max_length=200, null=True, blank=True)
    quantity = models.IntegerField(_("Quantiy"), default=0)
    slug = models.SlugField(_("Slug"), null=True, blank=True)

    objects = PollManager()

    class Meta:
        ordering = ('-pk',)

    def get_avg_reviews(self):
        avg = self.product_review.aggregate(myavg=Avg('rate'))
        return avg

    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"slug":self.slug})



    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

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
    image = models.ImageField(_("Image"), upload_to='brand/', null=True, blank=True)
    slug = models.SlugField(_("Slug"), blank=True)

    def get_absolute_url(self):
        return reverse("products:brand_detail", kwargs={"slug":self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    image = models.ImageField(_("Image"), upload_to='category')

    def get_absolute_url(self):
        return reverse("products:category_detail", kwargs={"slug":self.slug})

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, verbose_name=_(
        "Product"), related_name='product_review', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_(
        "User"), related_name='review_author', on_delete=models.SET_NULL, null=True)
    review = models.TextField(_("Review"), max_length=500)
    rate = models.IntegerField(_("Rate"), validators=[
                               MaxValueValidator(5), MinValueValidator(0)])
    created_at = models.DateTimeField(_("Created at"), default=timezone.now)
    

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'
