from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.api_endpoints.products.CategoriesList.serializers import CategoryListSerializer
from apps.products.models import Category


@api_view(['GET'])
def category_list_view(request):
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)
