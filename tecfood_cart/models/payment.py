from django.db import models
from .order_dish import OrderDish
from datetime import datetime

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('CARD', 'Card'),
        ('PAYPAL', 'PayPal'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('FAILED', 'Failed'),
        ('COMPLETED', 'Completed'),
    ]

    payment_id = models.AutoField(primary_key=True)
    order_dish = models.ForeignKey(OrderDish, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=6, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'payment'