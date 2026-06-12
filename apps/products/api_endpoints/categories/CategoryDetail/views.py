from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from apps.products.api_endpoints.categories.CategoryDetail.serializers import CategoryDetailSerializer
from apps.products.models import Category

@extend_schema(responses=CategoryDetailSerializer)
@api_view(['GET'])
def category_detail_view(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=404)

    serializer = CategoryDetailSerializer(category)
    return Response(serializer.data)
