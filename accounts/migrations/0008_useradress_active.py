# Generated by Django 3.2 on 2023-01-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_userphonenumber_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='useradress',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
    ]
