from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.category.api_endpoints.category.CategoryUpdateDestroy.serializers import CategoryUpdateDestroySerializers
from apps.category.models import Category

@api_view(['PATCH', 'DELETE'])
def category_update_view(request, pk):
    category = Category.objects.get(pk = pk)
    if category:
        if request.method == 'PATCH':
             serializer = CategoryUpdateDestroySerializers(category, data=request.data, partial=True)

             if serializer.is_valid():
                    product = serializer.save()
                    return Response(CategoryUpdateDestroySerializers(product).data)
             return Response(serializer.errors, status=400)
        elif request.method == 'DELETE':
             category.delete()
             return Response(status=204)
    else:
         return Response({'error':'category not found'}, status=404)