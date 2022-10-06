from itertools import product
from msilib.schema import ListView
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.urls import reverse
from products.forms import ReviewForm
from .models import Brand, Category, Product, ProductImages, Review
from django.db.models import Count
from django.contrib.auth.decorators import login_required
# Creat your views here.


class ProductList(ListView):
    model = Product
    paginate_by = 50


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        myproduct = self.get_object()
        context = super().get_context_data(**kwargs)
        context["images"] = ProductImages.objects.filter(product=myproduct)
        context["reviews"] = Review.objects.filter(product=myproduct)
        context['related'] = Product.objects.filter(
            category=myproduct.category)[:10]
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
    



class BrandDetail(DetailView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        #context["brands"] = Brand.objects.annotate(product_count=Count('product_brand'))
        context["brand_products"] = Product.objects.filter(brand=brand)
        return context



def add_review(request,slug):
    print('in review')
    product = Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['rate'])
            myform = form.save(commit=False)
            myform.user = request.user 
            myform.product = product 
            myform.save()
    
            return redirect(reverse('products:product_detail', kwargs={'slug': slug}))
    



@login_required
def add_to_favorites(request):
    prodcut_id = request.POST['productid']
    
    product = Product.objects.get(id=prodcut_id)

    if product in request.user.Profile.favorites.all():
        request.user.Profile.favorites.remove(product)
    else:
        request.user.Profile.favorites.add(product)