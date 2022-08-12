from django.urls import path
from .views import BrandList, CategoryList, ProductList, ProductDetail

app_name = 'products'


urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('category/', CategoryList.as_view(), name='category_list'),
    path('brand/', BrandList.as_view(), name='brand_list'),
    path('<slug:slug>', ProductDetail.as_view(), name='product_detail'),
]