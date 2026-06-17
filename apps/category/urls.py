from django.urls import path

from apps.category.api_endpoints.category.CategoryList.views import CategoryListView
from apps.category.api_endpoints.category.CategoryCreat.views import CreateCategoryView
from apps.category.api_endpoints.category.CategoryDetail.views import CategoryDetailView
from apps.category.api_endpoints.category.CategoryUpdateDestroy.views import CategoryDestroyView,  CategoryUpdateView

urlpatterns = [
    path('', CategoryListView.as_view(), name='get-category'),
    path('create/', CreateCategoryView.as_view(), name='category-create'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='get-detail'),
    path('<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('<int:pk>/delete/', CategoryDestroyView.as_view(), name='category-delete'),
]       