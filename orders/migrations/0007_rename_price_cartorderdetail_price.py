# Generated by Django 3.2 on 2022-08-27 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_cartorderdetail_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartorderdetail',
            old_name='Price',
            new_name='price',
        ),
    ]
