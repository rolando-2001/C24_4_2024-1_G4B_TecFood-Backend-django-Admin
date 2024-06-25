from django.db import models
from tecfood_dish.models import Dish
from tecfood_admin.models import User

class CartDish(models.Model):
    cart_id=models.AutoField(primary_key=True)
    quantity=models.IntegerField()
    dish=models.ForeignKey(Dish, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart_dish'

 
    


