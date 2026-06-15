from django.urls import path

from apps.orders.api_endpoints.orders.OrderCreate.views import CreateOrderView
from apps.orders.api_endpoints.orders.OrderList.views import OrderListAPiView
from apps.orders.api_endpoints.orders.OrderDetail.views import OrderDetailView
from apps.orders.api_endpoints.orders.OrderUpdateDestroy.views import OrderUpdateDestroyView, OrderDeleteView

urlpatterns = [
    path('', OrderListAPiView.as_view(), name='order-list'),
    path('create/', CreateOrderView.as_view(), name='order-create'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('<int:pk>/update/', OrderUpdateDestroyView.as_view(), name='order-update'),
    path('<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
]
