from rest_framework import serializers

from apps.category.models import Category

class CategoryUpdateDestroySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'