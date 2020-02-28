from django.shortcuts import render
from rest_framework import generics
from shopApp.serializers import ProductListSerializer, ProductDetailSerializer, ProductDestroySerializer,ProductUpdateSerializer, ProductCreateSerializer, UserSerializer,  UserCreateSerializer, CustomerSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework import generics,mixins
import requests
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from shopApp.models import Product ,Customer
from django.utils import timezone
from django.http import HttpResponse
from allauth.account.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import permissions
# from shopApp.permissions import IsOwnerOrReadOnly
# from rest_framework.permissions import IsAuthenticated

# Create your views here.

# @login_required
def productListView(request):
	return render(request, 'shopApp/home.html')


class ProductList(generics.ListAPIView):
	queryset = Product.objects.all()
	# permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	serializer_class=ProductListSerializer


class ProductDetail(generics.RetrieveAPIView):
	queryset = Product.objects.all()
	#permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	def get(self, request, pk, format=None):
		product = self.get_object()
		serializer = ProductDetailSerializer(product)
		return Response(serializer.data)


class ProductDestroy(generics.DestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductDestroySerializer

@method_decorator(csrf_exempt,name='dispatch')
class ProductCreateView(generics.CreateAPIView):
	# permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	# permission_classes = (IsAuthenticated,)
	queryset = Product.objects.all()
	serializer_class = ProductCreateSerializer

	def perform_create(self, serializer):
	   serializer.save(owner=self.request.user)



@method_decorator(csrf_exempt,name='dispatch')
class ProductUpdateView(generics.UpdateAPIView):
	# permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	# permission_classes = (IsAuthenticated,)
	queryset = Product.objects.all()
	serializer_class = ProductUpdateSerializer
	def perform_update(self, serializer):
	   serializer.save(owner=self.request.user)

	def update(self, request, *args, **kwargs):
		partial = True
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=request.data, partial=partial)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		return Response(serializer.data)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class CustomerDetail(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# class ProductWithCustomer(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductWithCustomerSerializers


# class ProductWithUser(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductWithUserSerializers
