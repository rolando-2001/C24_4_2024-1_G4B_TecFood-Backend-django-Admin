from rest_framework import serializers
from tecfood_dish.models import Dish, DishCategory


class DishSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(source='dish_category.name')
    dish_category_id = serializers.PrimaryKeyRelatedField(
        queryset=DishCategory.objects.all(),
        source='dish_category',
        
    )

    class Meta:
        model = Dish
        fields = [
            'dish_id', 
            'name', 
            'img_url', 
            'stock', 
            'description', 
            'price', 
            'dish_category_id', 
            'category',
            
        ]
