from rest_framework import serializers
from django.contrib.auth.models import User
from shopApp.models import Product, Cart, Order


class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'products']


class ProductListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = ['id', 'item_name','owner']


class ProductDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = '__all__'


class ProductDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductUpdateSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(required=False)
    item_detail = serializers.CharField(required=False)
    item_image = serializers.ImageField(max_length=None, use_url=True,required=False)
    item_price = serializers.FloatField(required=False)
    class Meta:
        model = Product
        fields = '__all__'
