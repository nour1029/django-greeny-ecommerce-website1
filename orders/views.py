from django.shortcuts import render
from .models import CartOrder, CartOrderDetail, Order, Coupon
from accounts.models import UserPhoneNumber, UserAdress
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.shortcuts import get_object_or_404
from django.utils.timezone import datetime
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)

    page = request.GET.get('page', 1)
    paginator = Paginator(orders, 12)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:  
        orders = paginator.page(paginator.num_pages)

    context = {'orders': orders, 'page':page}
    return render(request, 'orders/order_list.html', context)


@login_required
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
        cart = CartOrder.objects.get(user=request.user, order_status='Inprogress')
        cart_detail = CartOrderDetail.objects.filter(cart=cart.id)

        html = render_to_string('include/cart_side.html', {'cart':cart, 'cart_detail':cart_detail})
        cart_total = cart.get_total()
        cart_count = cart.get_count()

        return JsonResponse({'result':html, 'total':cart_total, 'count':cart_count})

@login_required
def delete_from_cart(request):
    if request.method == "POST":
        cartdetail_id = int(request.POST["order_id"])
        product = CartOrderDetail.objects.get(pk=cartdetail_id).delete()
        
        cart = CartOrder.objects.get(user=request.user, order_status='Inprogress')
        cart_detail = CartOrderDetail.objects.filter(cart=cart.id)

        html = render_to_string('include/cart_side.html', {'cart':cart, 'cart_detail':cart_detail})
        cart_total = cart.get_total()
        cart_count = cart.get_count()

        return JsonResponse({'result':html, 'total':cart_total, 'count':cart_count})

@login_required
def delete_from_checkout(request):
    if request.method == "POST":
        cartdetail_id = int(request.POST["order_id"])
        product = CartOrderDetail.objects.get(pk=cartdetail_id).delete()
        
        cart = CartOrder.objects.get(user=request.user, order_status='Inprogress')
        cart_detail = CartOrderDetail.objects.filter(cart=cart.id)

        cartside_html = render_to_string('include/cart_side.html', {'cart':cart, 'cart_detail':cart_detail})
        checkout_html = render_to_string('include/real-time/checkout_products_section.html', {'cart_detail':cart_detail})
        cart_count = cart.get_count()
        cart_total = cart.get_total()

        return JsonResponse({'cartside':cartside_html, 'checkout':checkout_html, 'total':cart_total, 'count':cart_count})

@login_required
def checkout_page(request):
    cart = CartOrder.objects.get(user=request.user, order_status="Inprogress")
    cart_detail = CartOrderDetail.objects.filter(cart=cart)

    sub_total = cart.get_total()
    delivery_fee = 25
    total = sub_total + delivery_fee
    discount_value = 0

    today_date = datetime.today().date()

    if request.method == "POST":
        print('post')
        coupon_code = get_object_or_404(Coupon, code=request.POST['code'])
        if coupon_code :
            if coupon_code.quantity > 0 and coupon_code.to_date>= today_date >= coupon_code.from_date:
                print('coupon valid')
                discount_value = cart.get_total() / 100 * coupon_code.value
                total = cart.get_total() - discount_value + delivery_fee
                html = render_to_string('include/total.html', {'sub_total':sub_total, 'delivery_fee':delivery_fee, 'discount_value':discount_value, 'total':total, 'coupon_code':coupon_code, request:request})
                return JsonResponse({'result':html})

    numbers = UserPhoneNumber.objects.filter(user=request.user)
    user_adress = UserAdress.objects.filter(user=request.user)


    context = {
        'cart_detail':cart_detail,
        'sub_total':sub_total,
        'delivery_fee':delivery_fee,
        'discount_value':discount_value,
        'total':total,
        'numbers':numbers,
        'user_adress':user_adress,
    }
    return render(request, 'orders/checkout.html', context)


@login_required
def invoice(requset, pk):
    order = Order.objects.get(pk=pk)
    context = {'order':order}
    return render(requset, 'orders/invoice.html', context)