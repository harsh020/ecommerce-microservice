from django.contrib import admin

from product.product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
