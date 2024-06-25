from  rest_framework import viewsets
from tecfood_dish.models import DishCategory
from tecfood_dish.serializers import DishCategorySerializer

class DishCategoryViewSet(viewsets.ModelViewSet):
    queryset = DishCategory.objects.all()
    serializer_class = DishCategorySerializer
    