from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from apps.products.api_endpoints.products.ProductList.serializers import ProductListSerializer
from apps.products.models import Product


# @api_view(['GET'])
# def product_list_view(request):
#     products = Product.objects.all()
#     serializer = ProductListSerializer(products, many=True)
#     return Response(serializer.data)

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category='Electronics')
        return queryset