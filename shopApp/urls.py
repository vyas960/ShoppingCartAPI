from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from shopApp import views

urlpatterns = [
    #path('', views.api_root),
    path('', views.ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('home/', views.homeView),

    #path('<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    #path('product/<int:pk>/', views.ProductDetail.as_view()),
    #path('list/', views.ProductListAPIView.as_view()),
    path('products/', views.ProductList.as_view()),
    # path('products/<int:pk>/', views.ProductDetail.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
