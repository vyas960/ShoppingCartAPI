from rest_framework import serializers
from django.contrib.auth.models import User
from shopApp.models import Product, Cart, Order, Customer



class ProductListSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = ['id', 'item_name']


class ProductDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = '__all__'


class ProductDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

def priceValidation(price):
    print('validations by using validator')
    if price < 50000:
        raise serializers.ValidationError('PRICE MUST BE MORE THAN 5000 RS')
def nameValidation(name):
    print('validations by using validator')
    var=' '
    if var in name:
        raise serializers.ValidationError('NAME CAN NOT INCLUDE WHITE SPACE')

class ProductCreateSerializer(serializers.ModelSerializer):
    item_price=serializers.FloatField(validators=[priceValidation,])
    item_name=serializers.CharField(validators=[nameValidation,])
    class Meta:
        model = Product
        fields = '__all__'


class ProductUpdateSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(required=False)
    item_detail = serializers.CharField(required=False)
    item_image = serializers.ImageField(max_length=None, use_url=True,required=False)
    item_price = serializers.FloatField(required=False)
    #item_price = serializers.FloatField(required=False)
    class Meta:
        model = Product
        #fields = '__all__'
        exclude = ('customer',)


class UserSerializer(serializers.ModelSerializer):
    #products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username','email']

class CustomerSerializer(serializers.ModelSerializer):
    #products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    class Meta:
        model = Customer
        fields = '__all__'



class UserCreateSerializer(serializers.ModelSerializer):
    #products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    class Meta:
        model = User
        fields = '__all__'


class ProductWithUserSerializers(serializers.ModelSerializer):
    owner= UserSerializer()
    customer = CustomerSerializer()
    class Meta:
       model =Product
       fields = ('id','item_name','owner','customer')
