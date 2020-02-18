from rest_framework import serializers
from django.contrib.auth.models import User
from shopApp.models import Product, Cart, Order

class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'products','owner']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'item_name']

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields='__all__'
