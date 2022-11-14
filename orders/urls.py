from pathlib import Path
from django.urls import path
from .views import add_to_cart, order_list, checkout_page, delete_from_cart
from .api import CartDetailDeleteAPI, CartDetailListAPI

app_name = "orders"


urlpatterns = [
    path("", order_list, name="order_list"),
    path("checkout/", checkout_page, name="checkout"),
    path("cart/add", add_to_cart, name="add_to_cart"),
    path("cart/delete/", delete_from_cart, name="delete_from_cart"),



    path("api/cart/", CartDetailListAPI.as_view(), name="cart_detail_list"),
    path("api/cart/delete/<int:pk>", CartDetailDeleteAPI.as_view(), name="cart_detail_delete_api"),
]
