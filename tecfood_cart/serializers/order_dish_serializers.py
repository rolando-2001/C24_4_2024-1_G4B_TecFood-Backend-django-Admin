from rest_framework import serializers

from tecfood_cart.models import OrderDish
from tecfood_admin.models import User

class OrderDishSerializer(serializers.ModelSerializer):
    order_user = serializers.StringRelatedField(source='user.first_name')
    #status_choices = serializers.SerializerMethodField()
    user_id=serializers.PrimaryKeyRelatedField(queryset=User.objects.all() ,source='user',)
   

    class Meta:
        model = OrderDish
        fields = ['order_id', 
                  'total', 
                  'status',
                  'user_id', 
                  'order_user',
                  'invoice_report_url',
                  'order_date']



   # def get_status_choices(self, obj):
        #return OrderDish.STATUS_CHOICES