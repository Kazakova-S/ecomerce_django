from django.urls import path
from apps.orders.api_endpoints.order.OrdersList.views import order_list

urlpatterns = [
    path('', order_list, name='order_list'),
]
