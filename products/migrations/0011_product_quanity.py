# Generated by Django 3.2 on 2022-08-15 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quanity',
            field=models.IntegerField(default=0, verbose_name='Quantiy'),
        ),
    ]
