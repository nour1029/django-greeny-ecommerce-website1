from django.db import models
from utils.code_generator import generate_code
from django.utils.translation import gettext as _
from django.utils import timezone
from products.models import Product
from django.contrib.auth.models import User
from django.db.models import Count, Sum
# Create your models here.


STATUS_CHOICES = (
    ('Recieved', _('Recieved')),
    ('Processed', _('Processed')),
    ('Shipped', _('Shipped')),
    ('Delivered', _('Delivered')),
)


CART_STATUS_CHOICES = (
    ('Inprogress', 'Inprogress'),
    ('Completed', 'Completed'),
)


class CartOrder(models.Model):
    user = models.ForeignKey(User, verbose_name=_(
        "User"), related_name='user_cart', on_delete=models.SET_NULL, null=True)
    code = models.CharField(_("Code"), max_length=8, default=generate_code)
    order_status = models.CharField(
        _("Order Status"), choices=CART_STATUS_CHOICES, max_length=50)
    order_time = models.DateTimeField(_("Order Time"), default=timezone.now)
    delivery_time = models.DateTimeField(
        _("Delivery Time"), null=True, blank=True)

    
    def get_total(self):
        total  = 0
        cart_detail = self.cart_detail.all()
        for product in cart_detail:
            total += product.total
        return total

    def get_count(self):
        total_count = self.cart_detail.count()
        return total_count

    def __str__(self):
        return self.code


class CartOrderDetail(models.Model):
    cart = models.ForeignKey(CartOrder, verbose_name=_(
        "Order"), related_name='cart_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_(
        "Product"), related_name='cart_product', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(_("Quantity"), default=0)
    price = models.FloatField(_("Price"), default=0)
    total = models.FloatField(_("Total"), default=0)

    def __str__(self):
        return str(self.cart)








class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=_(
        "User"), related_name='user_orders', on_delete=models.SET_NULL, null=True)
    code = models.CharField(_("Code"), max_length=8, default=generate_code)
    order_status = models.CharField(
        _("Order Status"), choices=STATUS_CHOICES, max_length=50)
    sub_total = models.FloatField(_("Sub Total"))
    discount = models.FloatField(_("Discount"))
    delivery_fee = models.FloatField(_("Delivery Fee"), default=15)
    total = models.FloatField(_("Total"))
    delivery_location = models.CharField(_("Delivery Location"), max_length=200)
    order_time = models.DateTimeField(_("Order Time"), default=timezone.now)
    delivery_time = models.DateTimeField(
        _("Delivery Time"), null=True, blank=True)

    def get_items_count(self):
        count = self.order_detail.aggregate(count=Count('quantity'))
        return count['count']

    def __str__(self):
        return self.code


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, verbose_name=_(
        "Order"), related_name='order_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_(
        "Product"), related_name='order_product', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(_("Quantity"))
    price = models.FloatField(_("Price"))

    def __str__(self):
        return f"{str(self.order)} - {self.product}"

    
class Coupon(models.Model):
    code = models.CharField(_("Code"), max_length=20)
    from_date = models.DateField(_("From Date"), default=timezone.now)
    to_date = models.DateField(_("To Date"), default=timezone.now)
    quantity = models.IntegerField(_("Quantity"))
    is_valid = models.BooleanField(_("Is Valid"), default=True)
    value = models.FloatField(_("Value"))

    def __str__(self):
        return self.code








