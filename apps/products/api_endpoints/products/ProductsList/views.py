from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from apps.products.api_endpoints.products.ProductsList.serializers import ProductListSerializer
from apps.products.models import Product

@extend_schema(responses=ProductListSerializer(many=True))
@api_view(['GET'])
def product_list_view(request):
    products = Product.objects.all()
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)
