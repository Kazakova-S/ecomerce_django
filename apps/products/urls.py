from django.urls import path
from apps.products.api_endpoints.products.ProductsList.views import product_list_view
from apps.products.api_endpoints.products.ProductCreate.views import product_create_view
from apps.products.api_endpoints.products.ProductUpdateDestroy.views import product_update_destroy_view
from apps.products.api_endpoints.products.CategoriesList.views import category_list_view
from apps.products.api_endpoints.products.CategoryCreate.views import category_create_view

urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('create/', product_create_view, name='product_create'),
    path('<int:pk>/', product_update_destroy_view, name='product_update_destroy'),
    path('categories/', category_list_view, name='category-list'),
    path('categories/create/', category_create_view, name='category-create'),
]
