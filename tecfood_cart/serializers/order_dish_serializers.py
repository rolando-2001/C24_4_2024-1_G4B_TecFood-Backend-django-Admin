from rest_framework import serializers

from tecfood_cart.models import OrderDish

class OrderDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDish
        fields = '__all__'