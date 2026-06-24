from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from apps.orders.api_endpoints.orders.filters import ProductFilter 

from apps.orders.api_endpoints.orders.OrderList.serializers import OrderListSerializer
from apps.orders.models import Order
from apps.products.pagination import CustomLimitOffsetPagination

# @api_view(['GET'])
# def order_list_view(request):
#     orders = Order.objects.all()
#     serializer = OrderListSerializer(orders, many=True)
#     return Response(serializer.data)


class OrderListAPiView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(address = 'Tashkent')
    #     return queryset
