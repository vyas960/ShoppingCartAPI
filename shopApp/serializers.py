from rest_framework import serializers
from django.contrib.auth.models import User
from shopApp.models import Product, Cart, Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields='__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields='__all__'
