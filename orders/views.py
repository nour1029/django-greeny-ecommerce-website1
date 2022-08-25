from django.shortcuts import render
from .models import Order
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)

    context = {'orders': orders}
    return render(request, 'orders/order_list.html', context)
