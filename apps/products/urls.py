from django.urls import path
from apps.products.api_endpoints.products.ProductList.views import product_list_view
from apps.products.api_endpoints.products.ProductCreate.views import product_create_view
from apps.products.api_endpoints.products.ProductDetail.views import product_detail_view
from apps.products.api_endpoints.products.ProductUpdateDestroy.views import product_update_view
urlpatterns = [
    path('',product_list_view, name='product-list'),
    path('create/',product_create_view, name = 'product-create'),
    path('<int:pk>/', product_detail_view, name='product-detail'),
    path('<int:pk>/update/',product_update_view, name = 'product-update'),
    path('<int:pk>/delete/',product_update_view, name = 'product-delete'),
]
