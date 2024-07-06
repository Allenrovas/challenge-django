from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.

    Attributes:
        model (Product): The Product model that the serializer works with.
        fields (list): The fields from the Product model that should be included in the serialized representation.
    """

    class Meta:
        model = Product
        fields = ["id", "name", "price", "quantity"]
