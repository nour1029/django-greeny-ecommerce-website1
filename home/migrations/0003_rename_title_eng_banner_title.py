# Generated by Django 3.2 on 2023-01-20 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_title_banner_title_eng'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='title_eng',
            new_name='title',
        ),
    ]
