# Generated by Django 4.2.14 on 2024-08-02 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cute', '0003_angelsimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycuteangel',
            name='title_day_img',
        ),
    ]