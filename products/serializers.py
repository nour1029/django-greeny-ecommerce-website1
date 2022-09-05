from unicodedata import category
from rest_framework import serializers
from .models import Brand, Category, Product, Review



class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField()
    # brand = serializers.StringRelatedField()

    # category = serializers.HyperlinkedRelatedField(
    #     read_only = True,
    #     view_name = 'products:category_detail_api',
    # )

    price_with_tax = serializers.SerializerMethodField(method_name='price_tax')

    def price_tax(self, product:Product):
        return product.price * 1.1

    class Meta:
        model = Product
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Review
        fields = ['user', 'review', 'rate']



class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    price_with_tax = serializers.SerializerMethodField(method_name='price_tax')
    reviews = ReviewSerializer(source='product_review', many=True)

    # category = serializers.HyperlinkedRelatedField(
    #     read_only = True,
    #     view_name = 'products:category_detail_api',
    # )

    def price_tax(self, product:Product):
        return product.price * 1.1

    class Meta:
        model = Product
        fields = ['name' ,'brand','category','price_with_tax','reviews']




class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(source='product_category', many=True)

    class Meta:
        model = Category
        fields = ['name', 'image', 'products']


class BrandSerializer(serializers.ModelSerializer):
    products = ProductSerializer(source='product_brand', many=True)

    class Meta:
        model = Brand
        fields = ['name', 'image']