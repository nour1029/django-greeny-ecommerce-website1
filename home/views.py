import re
from django.shortcuts import render
from .models import Banner
from products.models import Brand, Category, Product, Review
from django.db.models import Count

# Create your views here.


def home(request):
    banners = Banner.objects.filter(active=True)
    categories = Category.objects.all()
    featured = Product.objects.filter(flag='Featured')[:6]
    new = Product.objects.filter(flag='New')[:6]
    brands = Brand.objects.all().annotate(product_count=Count('product_brand'))[:6]
    reviews = Review.objects.filter(rate=5)[:4]

    context = {
        'banners': banners,
        'categories': categories, 
        'featured': featured, 
        'new':new, 
        'brands':brands,
        'reviews':reviews,
        }
        
    return render(request, 'home/index.html', context)
