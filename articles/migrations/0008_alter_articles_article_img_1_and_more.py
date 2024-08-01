# Generated by Django 4.2.14 on 2024-07-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_articles_articles_text_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article_img_1',
            field=models.ImageField(blank=True, null=True, upload_to='image/articles_description_img/', verbose_name='Картинка 1'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='article_img_2',
            field=models.ImageField(blank=True, null=True, upload_to='image/articles_description_img/', verbose_name='Картинка 2'),
        ),
    ]