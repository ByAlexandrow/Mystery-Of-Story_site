# Generated by Django 4.2.13 on 2024-07-24 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_articles_article_img_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesimage',
            name='about_us',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='articles.articles', verbose_name='Статья'),
        ),
    ]