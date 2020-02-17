from django.shortcuts import render
from shopApp.serializers import ProductSerializer
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from shopApp.serializers import UserSerializer
from rest_framework import generics,mixins
from rest_framework import permissions
from shopApp.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
import requests
#from django.views.generic import ListView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from shopApp.models import Product
from django.utils import timezone
from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here.
def homeView(request):
	return render(request,'shopApp/index.html')

#this view provide list of products........
class ProductListView(ListView):
	model = Product
	# paginate_by = 5
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context


class ProductDetail(APIView):
	# permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

	def get_object(self, pk):
		try:
			return Product.objects.get(pk=pk)
		except Product.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		product = self.get_object(pk)
		serializer = ProductSerializer(product)
		data = []
		data.append({
			"id": serializer.data["id"],
			"owner": serializer.data["owner"],
			"item_name": serializer.data["item_name"],
			"item_price": serializer.data["item_price"],
			"item_image": serializer.data["item_image"],
			"item_detail": serializer.data["item_detail"],
		})
		return Response(data)

	def post(self, request, pk, format=None):
		print("In post method")
		return HttpResponse("success")

# class ProductDetailView(DetailView):
#     model = Product
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context





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


# from rest_framework import viewsets
# class ProductDetailViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Product.objects.get(id=id)
#     serializer_class = UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    # serializer_class = UserSerializer
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'product': reverse('productlist', request=request, format=format),
#     })

# class ProductListAPIView(generics.ListAPIView):
# 	queryset=Product.objects.all()
# 	serializer_class=ProductSerializer


class ProductList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
	queryset = Product.objects.all()
	serializer_class= ProductSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
	permission_classes = (IsAuthenticated,)

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


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
#
