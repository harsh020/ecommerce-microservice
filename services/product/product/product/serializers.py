from rest_framework import serializers

from product.product.models import Product
from product.review.models import Review


class ProductSerializer(serializers.ModelSerializer):
    def find_by_slug(self, slug):
        instance = Product.objects.get(slug=slug)
        return instance

    class Meta:
        model = Product
        exclude = ('is_deleted',)


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('is_deleted', 'product',)


class ProductDetailSerializer(ProductSerializer):
    reviews = ProductReviewSerializer(source='product_reviews', many=True)

    def find_by_slug(self, slug):
        instance = Product.objects.get(slug=slug)
        return instance

    class Meta:
        model = Product
        exclude = ('is_deleted',)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'image',)
