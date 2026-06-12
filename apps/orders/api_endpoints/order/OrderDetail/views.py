from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from apps.orders.api_endpoints.order.OrderDetail.serializers import OrderDetailSerializer
from apps.orders.models import Order

@extend_schema(responses=OrderDetailSerializer)
@api_view(['GET'])
def order_detail_view(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=404)

    serializer = OrderDetailSerializer(order)
    return Response(serializer.data)
