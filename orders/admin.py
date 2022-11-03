import imp
from django.contrib import admin

# Register your models here.
from .models import CartOrder, CartOrderDetail, Order, OrderDetail, Coupon


admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(CartOrder)
admin.site.register(CartOrderDetail)
admin.site.register(Coupon)
