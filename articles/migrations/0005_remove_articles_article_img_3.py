# Generated by Django 4.2.13 on 2024-07-25 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_articlesimage_about_us'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='article_img_3',
        ),
    ]