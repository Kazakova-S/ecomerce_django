from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from apps.products.api_endpoints.products.ProductUpdateDestroy.serializers import ProductUpdateDestroySerializer
from apps.products.models import Product

@extend_schema(request=ProductUpdateDestroySerializer, responses=ProductUpdateDestroySerializer)
@api_view(['PATCH'])
def product_update_view(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product topilmadi'}, status=404)

    serializer = ProductUpdateDestroySerializer(product, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@extend_schema(responses=None)
@api_view(['DELETE'])
def product_destroy_view(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product topilmadi'}, status=404)

    product.delete()
    return Response({'message': 'Product o\'chirildi'}, status=204)
