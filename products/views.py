from itertools import product
from msilib.schema import ListView
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.urls import reverse
from products.forms import ReviewForm
from .models import Brand, Category, Product, ProductImages, Review
from accounts.models import Profile
from django.db.models import Count, Avg, F, Q
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Creat your views here.


class ProductList(ListView):
    model = Product
    paginate_by = 50

    # def get_queryset(self):
    #     try:
    #         min_price = self.request.GET['min-price']
    #         max_price = self.request.GET['max-price']
    #         queryset = Product.objects.filter(price__gt=min_price, price__lt=max_price)
    #         html = render_to_string('products/include/product_list_div.html', {'product_list':queryset, self.request:self.request})
    #         return JsonResponse({'result':html})
    #     except:
    #         queryset = super().get_queryset()
        

    #     return queryset

def product_filter(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    rating = request.GET.getlist('rating[]')
    flag = request.GET.getlist('flag[]')
    brand = request.GET.getlist('brand[]')
    category = request.GET.getlist('category[]')

    products = Product.objects.all()

    # products = Product.objects.filter(Q(price__gte=50, price__lte=100) | Q(price__gte=500, price__lte=600))
    # print(rating)
    
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    if rating:
        query_list = []
        for rate in rating:
            rate = int(rate)
            rate_min = rate-0.5
            rate_max = rate+0.5
            query_list.append(f'Q(rate_avg__gte={rate_min}, rate_avg__lt={rate_max})')
        query_string = '|'.join(query_list)
        queryset = eval(query_string)
        products = products.annotate(rate_avg=Avg('product_review__rate')).filter(queryset)
    if flag:
        products = products.filter(flag__in=flag)
    if brand:
        products = products.filter(brand__in=brand)
    if category:
        products = products.filter(category__in=category)
        
    # products = Product.objects.filter(get_avg_reviews = 5)
    # print(products)

    # Pagination
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    try:
        product_list = paginator.page(page)
    except PageNotAnInteger:
        product_list = paginator.page(1)
    except EmptyPage:  
        product_list = paginator.page(paginator.num_pages)


    html = render_to_string('products/include/product_list_div.html', {'product_list':product_list, 'page':page, 'value':'True'}, request=request)
    # 'request=request' is for basic context_processors like 'user'

    return JsonResponse({'result':html})


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        myproduct = self.get_object()
        context = super().get_context_data(**kwargs)
        context["images"] = ProductImages.objects.filter(product=myproduct)
        context["reviews"] = Review.objects.filter(product=myproduct)
        # context['related'] = Product.objects.filter(category=myproduct.category)[:10]
        context['related'] = myproduct.tags.similar_objects()[:10]
        return context


class CategoryList(ListView):
    model = Category
    paginate_by = 12

    def get_queryset(self):
        queryset = Category.objects.all().annotate(
            product_count=Count('product_category'))
        return queryset
    

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["category_list"] = Category.objects.all().annotate(
    #         product_count=Count('product_category'))
    #     return context


class BrandList(ListView):
    model = Brand
    paginate_by = 12

    def get_queryset(self):
        queryset = Brand.objects.annotate(product_count=Count('product_brand'))
        return queryset
    



class BrandDetail(ListView):
    model = Product
    template_name = 'products/brand_detail.html'
    paginate_by = 12
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     brand = self.get_object()
    #     #context["brands"] = Brand.objects.annotate(product_count=Count('product_brand'))
    #     context["brand_products"] = Product.objects.filter(brand=brand)
    #     return context

    def get_queryset(self):
        self.brand_slug = self.kwargs['slug']
        queryset = Product.objects.filter(brand__slug=self.brand_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.brand_slug)
        return context
    

    

@login_required
def add_review(request,slug):
    product = Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['rate'])
            myform = form.save(commit=False)
            myform.user = request.user 
            myform.product = product 
            myform.save()

            reviews = Review.objects.filter(product=product)
            reviews_count = reviews.count()

            html = render_to_string('products/include/reviews.html', {'reviews':reviews}) # Render context data on page and returns html text
            return JsonResponse({'result' : html, 'reviews_count':reviews_count})


@login_required
def add_to_favorites(request):
    prodcut_id = request.POST['productid']
    
    product = Product.objects.get(id=prodcut_id)

    if product in request.user.Profile.favorites.all():
        liked = False
        request.user.Profile.favorites.remove(product)
    else:
        liked = True
        request.user.Profile.favorites.add(product)
    
    profile = Profile.objects.get(user=request.user)

    return JsonResponse({'result':liked, 'favorites_count':profile.get_favorites_count()})


@login_required
def remove_from_favorites(request):
    prodcut_id = request.POST['productId']
    product = Product.objects.get(id=prodcut_id)

    request.user.Profile.favorites.remove(product)

    html = render_to_string('include/real-time/wishlist-tablelist.html', {}, request=request)
    return JsonResponse({'result':html})