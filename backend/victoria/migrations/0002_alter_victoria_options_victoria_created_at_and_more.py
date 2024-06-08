# Generated by Django 4.2.13 on 2024-06-08 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('victoria', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='victoria',
            options={'ordering': ('-created_at',), 'verbose_name': 'Виктория', 'verbose_name_plural': 'Виктория'},
        ),
        migrations.AddField(
            model_name='victoria',
            name='created_at',
            field=models.DateField(auto_now=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='victoria',
            name='period',
            field=models.CharField(default='', max_length=50, verbose_name='Период'),
        ),
        migrations.AlterField(
            model_name='victoria',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название момента'),
        ),
    ]
