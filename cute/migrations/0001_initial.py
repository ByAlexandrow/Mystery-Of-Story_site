# Generated by Django 4.2.14 on 2024-08-01 16:11

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyCuteAngel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_day', models.CharField(max_length=40, verbose_name='Название дня')),
                ('title_day_img', models.ImageField(upload_to='image/angel/', verbose_name='Титульная картинка дня')),
                ('day_description', tinymce.models.HTMLField(blank=True, default='Текст статьи. 1 отступ. 100-130 слов. Шрифт: заголовки - 18, подзаголовки - 14, текст - 12, белый цвет.', verbose_name='Описание дня')),
                ('period', models.CharField(max_length=30, verbose_name='Приод отношений')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Ангел',
                'verbose_name_plural': 'Ангел',
                'ordering': ['-date'],
            },
        ),
    ]