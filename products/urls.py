from django.urls import path
from .views import BrandDetail, BrandList, CategoryList, ProductList, ProductDetail, add_to_favorites
from .api import BrandDetailAPI, BrandListAPI, ProductDetailAPI, ProductListAPI, CategoryDetailAPI, CategoryListAPI


app_name = 'products'


urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('add_to_wish/', add_to_favorites, name='add_to_favorites'),
    path('category/', CategoryList.as_view(), name='category_list'),
    path('brand/', BrandList.as_view(), name='brand_list'),
    path('<slug:slug>', ProductDetail.as_view(), name='product_detail'),
    path('brand/<slug:slug>', BrandDetail.as_view(), name='brand_detail'),



    # api urls
    path('api/', ProductListAPI.as_view()),
    path('api/<int:pk>', ProductDetailAPI.as_view()),
    path('api/category/', CategoryListAPI.as_view()),
    path('api/category/<int:pk>', CategoryDetailAPI.as_view(), name='category_detail_api'),
    path('api/brand', BrandListAPI.as_view()),
    path('api/brand/<int:pk>', BrandDetailAPI.as_view()),
]
