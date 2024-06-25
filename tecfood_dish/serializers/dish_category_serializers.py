from rest_framework import serializers
from tecfood_dish.models import DishCategory


class DishCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DishCategory
        fields = [
            'dish_category_id',
            'name']
        