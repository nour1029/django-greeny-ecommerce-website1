from .serializers import CartOrderDetailSerializer
from .models import CartOrderDetail
from rest_framework import generics



class CartDetailDeleteAPI(generics.DestroyAPIView):
    serializer_class = CartOrderDetailSerializer
    queryset = CartOrderDetail.objects.all()