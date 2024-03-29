from django.urls import path
from .views import product_filter, BrandDetail, BrandList, CategoryList, ProductList, product_list, ProductDetail, add_review, add_to_favorites, remove_from_favorites
from .api import BrandDetailAPI, BrandListAPI, ProductDetailAPI, ProductListAPI, CategoryDetailAPI, CategoryListAPI


app_name = 'products'


urlpatterns = [
    path('', product_list, name='product_list'),
    path('filter/', product_filter, name='product_filter'),
    path('add_to_wish/', add_to_favorites, name='add_to_favorites'),
    path('remove_from_wish/', remove_from_favorites, name='remove_from_wish'),
    path('category/', CategoryList.as_view(), name='category_list'),
    path('brand/', BrandList.as_view(), name='brand_list'),
    path('<slug:slug>', ProductDetail.as_view(), name='product_detail'),
    path('<slug:slug>/add-review', add_review, name='add_review'),
    path('brand/<slug:slug>', BrandDetail.as_view(), name='brand_detail'),



    # api urls
    path('api/', ProductListAPI.as_view()),
    path('api/<int:pk>', ProductDetailAPI.as_view()),
    path('api/category/', CategoryListAPI.as_view()),
    path('api/category/<int:pk>', CategoryDetailAPI.as_view(), name='category_detail_api'),
    path('api/brand', BrandListAPI.as_view()),
    path('api/brand/<int:pk>', BrandDetailAPI.as_view()),
]
