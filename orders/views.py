from django.shortcuts import render
from .models import CartOrder, CartOrderDetail, Order
from django.contrib.auth.decorators import login_required
from products.models import Product
# Create your views here.


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)

    context = {'orders': orders}
    return render(request, 'orders/order_list.html', context)



def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST['productid']
        quantity = request.POST['quantity']

        product = Product.objects.get(id=product_id)
        cart = CartOrder.objects.get(user=request.user, order_status='Inprogress')
        cart_detail, created = CartOrderDetail.objects.update_or_create(
            cart=cart,
            product=product,
            defaults = {
                'quantity':int(quantity),
                'price':product.price,
                'total':int(quantity) * product.price,
            }
        )
        # cart_detail.quantity = int(quantity)
        # cart_detail.price = product.price
        # cart_detail.total = int(quantity) * product.price
        # cart_detail.save()