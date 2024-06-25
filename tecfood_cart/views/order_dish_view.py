from rest_framework import viewsets
from tecfood_cart.models import OrderDish
from tecfood_cart.serializers import OrderDishSerializer

class OrderDishViewSet(viewsets.ModelViewSet):
    queryset = OrderDish.objects.all()
    serializer_class = OrderDishSerializer
    