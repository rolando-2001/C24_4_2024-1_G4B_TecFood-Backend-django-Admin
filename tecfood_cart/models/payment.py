from django.db import models
from .order_dish import OrderDish

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('CREDIT_CARD', 'Credit Card'),
        ('DEBIT_CARD', 'Debit Card'),
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
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')


    class Meta:
        db_table = 'payment'