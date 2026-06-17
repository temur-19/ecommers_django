from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from apps.category.models import Category
from apps.category.api_endpoints.category.CategoryCreat.serializers import CategoryCreatSerializers

# @api_view(['POST'])
# def category_creat_view(request):
#     serializers = CategoryCreatSerializers(data = request.data)
#     if serializers.is_valid():
#         category = serializers.save()
#         return Response(CategoryCreatSerializers(category).data , status=201)
#     return Response(serializers.errors, status=400)

class CreateCategoryView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreatSerializers