# Generated by Django 5.0.6 on 2024-06-25 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tecfood_cart', '0002_rename_cart_id_cartdish_cart_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartdish',
            old_name='dish_id',
            new_name='dish',
        ),
        migrations.RenameField(
            model_name='cartdish',
            old_name='user_id',
            new_name='user',
        ),
    ]