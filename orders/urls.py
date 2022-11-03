from pathlib import Path
from django.urls import path
from .views import add_to_cart, order_list, checkout_page


app_name = "orders"


urlpatterns = [
    path("", order_list, name="order_list"),
    path("checkout/", checkout_page, name="checkout"),
    path("cart/add", add_to_cart, name="add_to_cart"),
]
