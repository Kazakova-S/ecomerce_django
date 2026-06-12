from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from apps.orders.api_endpoints.order.OrdersList.serializer import OrderListSerializer
from apps.orders.models import Order

@extend_schema(responses=OrderListSerializer(many=True))
@api_view(['GET'])
def order_list_view(request):
    orders = Order.objects.all()
    serializer = OrderListSerializer(orders, many=True)
    return Response(serializer.data)
