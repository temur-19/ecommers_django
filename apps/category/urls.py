from django.urls import path

from apps.category.api_endpoints.category.CategoryList.views import get_category_view
from apps.category.api_endpoints.category.CategoryCreat.views import category_creat_view
from apps.category.api_endpoints.category.CategoryDetail.views import get_category_detail_view
from apps.category.api_endpoints.category.CategoryUpdateDestroy.views import category_update_view

urlpatterns = [
    path('',get_category_view, name='get-category'),
    path('create/',category_creat_view, name='category-creat'),
    path('<int:pk>/', get_category_detail_view, name='get-detail'),
    path('<int:pk>/update/', category_update_view, name = 'category-update'),
    path('<int:pk>/delete/', category_update_view, name='category-delete'),
]