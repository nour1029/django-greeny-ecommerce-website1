# Generated by Django 3.2 on 2022-08-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_brand_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='products/', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
