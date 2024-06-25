from django.db import models
from tecfood_dish.models import Dish
from .order_dish import OrderDish

class OrderDishItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_dish = models.ForeignKey(OrderDish, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    class Meta:
        db_table = 'order_dish_item'