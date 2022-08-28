from django.urls import path
from .views import BrandDetail, BrandList, CategoryList, ProductList, ProductDetail, add_to_favorites

app_name = 'products'


urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('add_to_wish/', add_to_favorites, name='add_to_favorites'),
    path('category/', CategoryList.as_view(), name='category_list'),
    path('brand/', BrandList.as_view(), name='brand_list'),
    path('<slug:slug>', ProductDetail.as_view(), name='product_detail'),
    path('brand/<slug:slug>', BrandDetail.as_view(), name='brand_detail'),
]
