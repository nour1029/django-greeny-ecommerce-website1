# Generated by Django 3.2 on 2023-01-10 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_alter_orderdetail_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_fee',
            field=models.FloatField(default=0, verbose_name='Delivery Fee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.FloatField(default=0, verbose_name='Discount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='sub_total',
            field=models.FloatField(default=0, verbose_name='Sub Total'),
            preserve_default=False,
        ),
    ]