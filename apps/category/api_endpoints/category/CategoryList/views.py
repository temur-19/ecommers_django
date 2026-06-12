from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.category.models import Category
from apps.category.api_endpoints.category.CategoryList.serializers import CategoryListSerializers

@api_view(['GET'])
def get_category_view(request):
    category = Category.objects.all()
    return Response(CategoryListSerializers(category, many = True).data,status=200)

