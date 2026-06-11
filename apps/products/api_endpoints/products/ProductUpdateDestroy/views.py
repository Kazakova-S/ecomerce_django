from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.products.api_endpoints.products.ProductsList.serializers import ProductListSerializer
from apps.products.models import Product

@api_view(['PATCH', 'DELETE'])
def product_update_destroy_view(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product topilmadi'}, status=404)

    if request.method == 'PATCH':
        serializer = ProductListSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return Response({'message': 'Product o\'chirildi'}, status=204)