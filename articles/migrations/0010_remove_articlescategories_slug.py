# Generated by Django 4.2.13 on 2024-07-13 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_articlescategories_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlescategories',
            name='slug',
        ),
    ]
