from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer



@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data

    return Response({'Sucsess':True, 'product list':data})



class ProductListAPI(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()



class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()