# Generated by Django 3.2 on 2023-01-04 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_product_before_discount_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='before_discount_price',
            new_name='price_before_discount',
        ),
    ]
