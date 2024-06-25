from django.db import models

class DishCategory(models.Model):
    dish_category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name
    
    class Meta:
          db_table = 'dish_category'
    
