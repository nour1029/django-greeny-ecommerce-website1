from rest_framework import PageNumberPagination



class ProductPagination(PageNumberPagination):
    page_size = 50