# Generated by Django 4.2.13 on 2024-06-08 15:01

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Victoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наша история')),
                ('our_story', tinymce.models.HTMLField(verbose_name='Вся наша история')),
            ],
            options={
                'verbose_name': 'Виктория',
                'verbose_name_plural': 'Виктория',
            },
        ),
    ]
