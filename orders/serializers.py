from rest_framework import serializers
from .models import CartOrderDetail


class CartOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartOrderDetail
        fields = '__all__'