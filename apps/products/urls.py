from django.urls import path
from apps.products.api_endpoints.products.ProductList.views import ProductListView
from apps.products.api_endpoints.products.ProductCreate.views import CreateProductView
from apps.products.api_endpoints.products.ProductDetail.views import  ProductDetailView
from apps.products.api_endpoints.products.ProductUpdateDestroy.views import ProductDestroyView, ProductUpdateView
urlpatterns = [
    path('',ProductListView.as_view(), name='product-list'),
    path('create/',CreateProductView.as_view(), name = 'product-create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/update/',ProductUpdateView.as_view(), name = 'product-update'),
    path('<int:pk>/delete/',ProductDestroyView.as_view(), name = 'product-delete'),
]

