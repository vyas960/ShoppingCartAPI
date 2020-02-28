from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from shopApp import views


urlpatterns = [
     path('', views.productListView),
     path('products/', views.ProductList.as_view(), name="ProductList"),
     path('products/<int:pk>/', views.ProductDetail.as_view(), name="ProducDetail"),
     path('products/<int:pk>/destroy/', views.ProductDestroy.as_view(), name="ProductDestroy"),
     path('create/', views.ProductCreateView.as_view(), name="ProductCreate"),
     path('update/<int:pk>/', views.ProductUpdateView.as_view(), name="ProductUpdate"),
     # path('pnu/<int:pk>/', views.ProductWithUser.as_view(), name="Product"),



     path('users/', views.UserList.as_view()),
     path('users/<int:pk>/', views.UserDetail.as_view()),
     path('createuser/', views.UserCreate.as_view()),
     path('customer/', views.CustomerDetail.as_view()),
     # path('pnc/', views.ProductWithCustomer.as_view()),
     #path('abc/<int:pk>/', views.ProductDetailabc.as_view()),
     # path('', views.api_root),
     # path('list/', views.ProductListView.as_view(), name='product-list'),
     # path('product/<int:pk>/', views.ProductDetail.as_view()),
     # path('list/', views.ProductListAPIView.as_view()),
     # path('detail/', views.productDetailView),

]

urlpatterns = format_suffix_patterns(urlpatterns)
