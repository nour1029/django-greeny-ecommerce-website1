from pathlib import Path
from django.urls import path
from .views import add_to_cart, order_list, checkout_page, invoice, delete_from_cart, delete_from_checkout
from .api import CartDetailDeleteAPI

app_name = "orders"


urlpatterns = [
    path("", order_list, name="order_list"),
    path("checkout/", checkout_page, name="checkout"),
    path("checkout/product/delete/", delete_from_checkout, name="delete_from_checkout"),
    path("invoice/<int:pk>", invoice, name="invoice"),
    path("cart/add", add_to_cart, name="add_to_cart"),
    path("cart/delete/", delete_from_cart, name="delete_from_cart"),



    path("api/cart/delete/<int:pk>", CartDetailDeleteAPI.as_view(), name="cart_detail_delete_api"),
]
