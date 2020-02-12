from django.shortcuts import render
from shopApp.serializers import ProductSerializer
from rest_framework.views import APIView
from shopApp.models import Product
from rest_framework.response import Response

# Create your views here.
class ProductList(APIView):
	def get(self, request, format= None):
		queryset = Product.objects.all()
		serializer= ProductSerializer(queryset, many=True)
		return Response(serializer.data)
	def post(self, request, format=None):
		serializer = ProductSerializer(data=request.data)
		if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class ProductDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Order.objects.get(pk=pk)
#         except Order.DoesNotExist:
#             raise Http404
#     def get(self, request, pk, format=None):
#         order = self.get_object(pk)
#         serializer = OrderSerializers(order)
#         return Response(serializer.data)
#     def put(self, request, pk, format=None):
#         order = self.get_object(pk)
#         serializer = OrderSerializers(order, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk, format=None):
#         order = self.get_object(pk)
#         order.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
