# Generated by Django 4.2.14 on 2024-08-01 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cute', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycuteangel',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовать'),
        ),
    ]
