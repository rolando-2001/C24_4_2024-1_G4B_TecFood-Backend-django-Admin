# Generated by Django 5.0.6 on 2024-06-25 10:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tecfood_dish', '0002_remove_dish_ima_url_dish_img_url'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CartDish',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('dish_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tecfood_dish.dish')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cart_dish',
            },
        ),
        migrations.CreateModel(
            name='OrderDish',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('invoice_report_url', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('PROCESSED', 'Processed'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'order_dish',
            },
        ),
    ]