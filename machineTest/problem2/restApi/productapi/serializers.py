from rest_framework import serializers
from .models import Product, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)
        depth = 1
class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True,required=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'color', 'images')
