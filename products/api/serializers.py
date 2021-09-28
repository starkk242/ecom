from django.db.models import query
from rest_framework import serializers

from products.models import Images, Product, Category



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('product_id','images',)

class ProductSerializer(serializers.ModelSerializer):
    images_list = ImageSerializer(many = True, )
    # category_list = CategorySerializer(many=True, )

    class Meta:
        model = Product
        fields = "__all__"
        lookup_field = "slug"

class CategorySerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # name = serializers.CharField()
    # product_list = ProductSerializer(many=True, )
    class Meta:
        model = Category
        fields = ("id", "name",)