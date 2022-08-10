from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Brand, Category, Product, ProductImages, Review
from django.db.models import Count
# Creat your views here.


class ProductList(ListView):
    model = Product
    paginate_by = 1


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        myproduct = self.get_object()
        context = super().get_context_data(**kwargs)
        context["images"] = ProductImages.objects.filter(product=myproduct)
        context["reviews"] = Review.objects.filter(product=myproduct)
        return context


class CategoryList(ListView):
    model = Category
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = Category.objects.all().annotate(
            product_count=Count('product_category'))
        return context


class BrandList(ListView):
    model = Brand
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.annotate(
            product_count=Count('product_brand'))
        return context
