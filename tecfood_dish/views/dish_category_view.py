from  rest_framework import viewsets
from tecfood_dish.models import DishCategory
from tecfood_dish.serializers import DishCategorySerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class DishCategoryViewSet(viewsets.ModelViewSet):
    queryset = DishCategory.objects.all()
    serializer_class = DishCategorySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name','dish_category_id']
    ordering = ['name']  # Ordenamiento por defecto
    