from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from apps.products.api_endpoints.categories.CategoryCreate.serializers import CategoryCreateSerializer
from apps.products.models import Category

@extend_schema(request=CategoryCreateSerializer, responses=CategoryCreateSerializer)
@api_view(['POST'])
def category_create_view(request):
    serializer = CategoryCreateSerializer(data=request.data)
    if serializer.is_valid():
        category = serializer.save()
        return Response(CategoryCreateSerializer(category).data, status=201)
    return Response(serializer.errors, status=400)
