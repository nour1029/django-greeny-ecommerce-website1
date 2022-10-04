from rest_framework.response import Response
from rest_framework import generics
import django_filters.rest_framework
from rest_framework.decorators import api_view
from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductDetailSerializer, ProductSerializer
from .pagination import ProductPagination
from .filters import ProductFilter



class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = ProductFilter


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
