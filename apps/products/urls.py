from django.urls import path
from apps.products.api_endpoints.products.ProductsList.views import product_list_view
from apps.products.api_endpoints.products.ProductCreate.views import product_create_view
from apps.products.api_endpoints.products.ProductDetail.views import product_detail_view
from apps.products.api_endpoints.products.ProductUpdateDestroy.views import product_update_view
from apps.products.api_endpoints.products.ProductUpdateDestroy.views import product_destroy_view
from apps.products.api_endpoints.categories.CategoriesList.views import category_list_view
from apps.products.api_endpoints.categories.CategoryCreate.views import category_create_view
from apps.products.api_endpoints.categories.CategoryDetail.views import category_detail_view
from apps.products.api_endpoints.categories.CategoryUpdateDestroy.views import category_update_view
from apps.products.api_endpoints.categories.CategoryUpdateDestroy.views import category_destroy_view

urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('create/', product_create_view, name='product_create'),
    path('<int:pk>/', product_detail_view, name='product-detail'),
    path('<int:pk>/update/', product_update_view, name='product-update'),
    path('<int:pk>/delete/', product_destroy_view, name='product-delete'),
    path('categories/', category_list_view, name='category-list'),
    path('categories/create/', category_create_view, name='category-create'),
    path('categories/<int:pk>/', category_detail_view, name='category-detail'),
    path('categories/<int:pk>/update/', category_update_view, name='category-update'),
    path('categories/<int:pk>/delete/', category_destroy_view, name='category-delete'),
]
