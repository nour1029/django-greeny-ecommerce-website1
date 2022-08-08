from django.contrib import admin

# Register your models here.
from .models import Product, Brand, Category, ProductImages, Review


class ProductImagesInline(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductImages)
admin.site.register(Review)
