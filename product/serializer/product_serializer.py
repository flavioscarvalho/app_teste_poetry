from rest_framework import serializers

from product.models.product import Product
from product.serializer.category_serializer import CategorySerilizer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerilizer(required=True, many = True)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'active',
            'category',
        ]