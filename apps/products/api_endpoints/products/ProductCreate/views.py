from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from apps.products.api_endpoints.products.ProductCreate.serializers import ProductCreateSerializer
from apps.products.models import Product


# @api_view(['POST'])

# def product_create_view(request):
#     serializer = ProductCreateSerializer(data=request.data)
#     if serializer.is_valid():
#             product = serializer.save()
#             return Response(ProductCreateSerializer(product).data, status=201)
#     return Response(serializer.errors, status=400)


class CreateProductView(CreateAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductCreateSerializer