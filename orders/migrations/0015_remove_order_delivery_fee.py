# Generated by Django 3.2 on 2023-01-10 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_alter_order_delivery_fee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_fee',
        ),
    ]
