import imp
from django.contrib import admin

# Register your models here.
from .models import CartOrder, CartOrderDetail, Order, OrderDetail


admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(CartOrder)
admin.site.register(CartOrderDetail)
