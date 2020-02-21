from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from shopApp import views

urlpatterns = [
     path('', views.productListView),
     path('products/', views.ProductList.as_view()),
     path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
     path('products/<int:pk>/destroy/', views.ProductDestroy.as_view(), ),
     path('create/', views.ProductCreateView.as_view(), ),
     path('update/<int:pk>/', views.ProductUpdateView.as_view(), ),

     #path('abc/<int:pk>/', views.ProductDetailabc.as_view()),
     # path('', views.api_root),
     # path('list/', views.ProductListView.as_view(), name='product-list'),
     # path('product/<int:pk>/', views.ProductDetail.as_view()),
     # path('list/', views.ProductListAPIView.as_view()),
     # path('detail/', views.productDetailView),
     path('users/', views.UserList.as_view()),
     path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
