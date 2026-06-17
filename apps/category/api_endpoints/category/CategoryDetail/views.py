from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView

from apps.category.api_endpoints.category.CategoryDetail.serializers import CategoryDetailSerializers
from apps.category.models import Category

# @api_view(['GET'])
# def get_category_detail_view(request, pk):
#     try:
#         category = Category.objects.get(pk = pk)
#     except Category.DoesNotExist:
#         return Response({'error': 'Category not found'}, status=404)
#     return Response(CategoryDetailSerializers(category).data, status=200)


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializers

    