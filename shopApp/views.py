from django.shortcuts import render
from rest_framework import generics
from shopApp.serializers import ProductListSerializer, ProductDetailSerializer, ProductDestroySerializer, ProductUpdateSerializer, ProductCreateSerializer
# from rest_framework.views import APIView
from rest_framework import status
from shopApp.forms import ProductCreateForm

from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
# from django.contrib.auth.models import User
# from shopApp.serializers import UserSerializer
from rest_framework import generics,mixins
from rest_framework import permissions
from shopApp.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
import requests
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from shopApp.models import Product
from django.utils import timezone
from django.http import HttpResponse
from allauth.account.decorators import login_required



# Create your views here.
@login_required
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


class ProductCreateView(generics.CreateAPIView):
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	permission_classes = (IsAuthenticated,)
	queryset = Product.objects.all()
	serializer_class = ProductCreateSerializer

	# def perform_create(self, serializer):
	#    serializer.save(owner=self.request.user)




class ProductUpdateView(generics.UpdateAPIView):
	# permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	# permission_classes = (IsAuthenticated,)
	queryset = Product.objects.all()
	serializer_class = ProductUpdateSerializer

	def update(self, request, *args, **kwargs):
		partial = True
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=request.data, partial=partial)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		return Response(serializer.data)




# class ProductUpdateView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductUpdateSerializer
#     # def get(self, request, *args, **kwargs):
#     #     return self.retrieve(request, *args, **kwargs)
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

	# def update(self, request, *args, **kwargs):
	# 	partial = kwargs.pop('partial', False)
	# 	self.object = None
	# 	try:
	# 		self.object = self.get_object()
	# 	except Http404:
    #         # If this is a PUT-as-create operation, we need to ensure that
    #         # we have relevant permissions, as if this was a POST request.
	# 		self.check_permissions(clone_request(request, 'POST'))
	# 		created = True
	# 		save_kwargs = {'force_insert': True}
	# 		success_status_code = status.HTTP_201_CREATED
	# 	else:
	# 		created = False
	# 		save_kwargs = {'force_update': True}
	# 		success_status_code = status.HTTP_200_OK
	#
	# 	serializer = self.get_serializer(self.object, data=request.data, partial=partial)
	#
	# 	if serializer.is_valid():
	# 		self.pre_save(serializer.object)
	# 		self.object = serializer.save(**save_kwargs)
	# 		self.post_save(self.object, created=created)
	# 		return Response(serializer.data, status=success_status_code)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)












# class ProductDetailabc(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductDetailSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

	# def post(self, request, pk, format=None):
	# 	print("In post method")
	# 	return HttpResponse("success")
	#
	# def put(self, request, pk, format=None):
	# 	product = self.get_object(pk)
	# 	serializer = ProductSerializer(product, data=request.data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	#
	# def delete(self, request, pk, format=None):
	# 	product = self.get_object(pk)
	# 	product.delete()
	# 	return Response(status=status.HTTP_204_NO_CONTENT)


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'product': reverse('productlist', request=request, format=format),
#     })

# class ProductList(APIView):
# 	permission_classes = (IsAuthenticated,)
# 	#permission_classes = [permissions.IsAuthenticatedOrReadOnly]
# 	def get(self, request, format= None):
# 		queryset = Product.objects.all()
# 		serializer= ProductSerializer(queryset, many=True)
# 		return Response(serializer.data)
#
# 	def post(self, request, format=None):
# 		serializer = ProductSerializer(data=request.data)
# 		if serializer.is_valid():
# 		    serializer.save()
# 		    return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# 	def perform_create(self, serializer):
# 		serializer.save(owner=self.request.user)
