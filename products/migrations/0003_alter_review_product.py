# Generated by Django 3.2 on 2022-08-10 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_reviews_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='product_review', to='products.product', verbose_name='Product'),
            preserve_default=False,
        ),
    ]
