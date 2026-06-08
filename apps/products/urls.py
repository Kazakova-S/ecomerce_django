from django.urls import path
from apps.products.api_endpoints.products.ProductsList.views import product_list

urlpatterns = [
    path('', product_list, name='product_list'),
]
