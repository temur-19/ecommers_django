from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


from apps.products.api_endpoints.products.ProductList.serializers import ProductListSerializer
from apps.products.models import Product
from apps.products.pagination import CustomLimitOffsetPagination
from apps.products.api_endpoints.products.filters import ProductFilter


# @api_view(['GET'])
# def product_list_view(request):
#     products = Product.objects.all()
#     serializer = ProductListSerializer(products, many=True)
#     return Response(serializer.data)

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    # def queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(category='Electronics')
    #     return queryset