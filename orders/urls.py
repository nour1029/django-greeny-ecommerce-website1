from pathlib import Path
from django.urls import path
from .views import add_to_cart, order_list


app_name = "orders"


urlpatterns = [
    path("", order_list, name="order_list"),
    path("cart/add", add_to_cart, name="add_to_cart"),
]
