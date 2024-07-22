from rest_framework import serializers

from product.models import Product
from product_serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True,many=True)
    total = serializers.SerializerMetaclass()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total
    
    class Meta:
        model=Product
        fields=['product','total']