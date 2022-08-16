from django.db import models
from utils.code_generator import generate_code
from django.utils.translation import gettext as _
from django.utils import timezone
from products.models import Product
from django.contrib.auth.models import User
# Create your models here.


STATUS_CHOICES = (
    ('Recieved', 'Recieved'),
    ('Processed', 'Processed'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
)


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=_(
        "User"), related_name='user_orders', on_delete=models.SET_NULL, null=True)
    code = models.CharField(_("Code"), max_length=8, default=generate_code)
    order_status = models.CharField(
        _("Order Status"), choices=STATUS_CHOICES, max_length=50)
    order_time = models.DateTimeField(_("Order Time"), default=timezone.now)
    delivery_time = models.DateTimeField(
        _("Delivery Time"), null=True, blank=True)

    def __str__(self):
        return self.code


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, verbose_name=_(
        "Order"), related_name='order_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_(
        "Product"), related_name='order_product', on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField(_("Quantity"))
    Price = models.FloatField(_("Price"))

    def __str__(self):
        return str(self.order)
