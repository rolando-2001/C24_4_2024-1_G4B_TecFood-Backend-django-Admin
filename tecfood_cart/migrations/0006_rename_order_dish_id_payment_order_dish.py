# Generated by Django 5.0.6 on 2024-06-25 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tecfood_cart', '0005_orderdishitem_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='order_dish_id',
            new_name='order_dish',
        ),
    ]
