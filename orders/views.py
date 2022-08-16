from django.shortcuts import render
from .models import Order
# Create your views here.


def order_list(request):
    orders = Order.objects.filter(user=request.user)

    context = {'orders': orders}
    return render(request, 'orders/order_list.html', context)
