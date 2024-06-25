from django.contrib import admin

from tecfood_dish.models import Dish, DishCategory
# Register your models here.
admin.site.register(Dish)
admin.site.register(DishCategory)