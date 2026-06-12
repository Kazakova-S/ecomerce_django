from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from apps.orders.api_endpoints.order.OrderUpdateDestroy.serializer import OrderUpdateSerializer
from apps.orders.models import Order


@extend_schema(request=OrderUpdateSerializer, responses=OrderUpdateSerializer)
@api_view(['PATCH'])
def order_update_view(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=404)

    serializer = OrderUpdateSerializer(order, data=request.data, partial=True)
    if serializer.is_valid():
        order = serializer.save()
        return Response(OrderUpdateSerializer(order).data)
    return Response(serializer.errors, status=400)


@extend_schema(responses=None)
@api_view(['DELETE'])
def order_destroy_view(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=404)

    order.delete()
    return Response(status=204)

