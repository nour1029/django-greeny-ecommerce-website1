from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductDetailSerializer, ProductSerializer




class ProductListAPI(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailAPI(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()




class BrandListAPI(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class BrandDetailAPI(generics.RetrieveAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()




class CategoryListAPI(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDetailAPI(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
