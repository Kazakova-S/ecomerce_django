from django.urls import path

from apps.orders.api_endpoints.order.OrderCreate.views import order_create_view
from apps.orders.api_endpoints.order.OrderDetail.views import order_detail_view
from apps.orders.api_endpoints.order.OrdersList.views import order_list_view
from apps.orders.api_endpoints.order.OrderUpdateDestroy.views import order_update_view
from apps.orders.api_endpoints.order.OrderUpdateDestroy.views import order_destroy_view


urlpatterns = [
    path('', order_list_view, name='order-list'),
    path('create/', order_create_view, name='order-create'),
    path('<int:pk>/', order_detail_view, name='order-detail'),
    path('<int:pk>/update/', order_update_view, name='order-update'),
    path('<int:pk>/delete/', order_destroy_view, name='order-delete'),
]
