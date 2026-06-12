from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from apps.products.api_endpoints.categories.CategoryUpdateDestroy.serializers import CategoryUpdateDestroySerializer
from apps.products.models import Category


@extend_schema(request=CategoryUpdateDestroySerializer, responses=CategoryUpdateDestroySerializer)
@api_view(['PATCH'])
def category_update_view(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category topilmadi'}, status=404)

    serializer = CategoryUpdateDestroySerializer(category, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@extend_schema(responses=None)
@api_view(['DELETE'])
def category_destroy_view(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category topilmadi'}, status=404)

    category.delete()
    return Response({'message': 'Category o\'chirildi'}, status=204)
