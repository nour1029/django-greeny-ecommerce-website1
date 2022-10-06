from django.contrib import admin
# Register your models here.
from .models import Product, Brand, Category, ProductImages, Review
from django_summernote.admin import SummernoteModelAdmin

from django.db.models import Avg


class ProductImagesInline(admin.TabularInline):
    model = ProductImages


class ProductAdmin(SummernoteModelAdmin):
    list_per_page = 50   # Pagination
    inlines = [ProductImagesInline]
    summernote_fields = '__all__'
    list_display = ['name', 'sku', 'rate_avg']

    def rate_avg(self, obj):
        return 0


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductImages)
admin.site.register(Review)
