# Generated by Django 4.2.13 on 2024-07-11 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_articlescategories_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlescategories',
            name='slug',
        ),
    ]
