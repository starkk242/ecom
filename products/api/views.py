from django.db.models.fields.related import create_many_to_many_intermediary_model
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProductSerializer, CategorySerializer
from products.models import Product, Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"
    search_fields = ["id", "name"]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["category__name", "name", "description"]

