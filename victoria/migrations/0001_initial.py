# Generated by Django 4.2.13 on 2024-06-21 11:58

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
                ('best_img', models.ImageField(upload_to='images/moments/', verbose_name='Фото дня')),
                ('title', models.CharField(max_length=100, verbose_name='Название момента')),
                ('our_story', tinymce.models.HTMLField(verbose_name='Вся наша история')),
                ('period', models.CharField(blank=True, max_length=50, null=True, verbose_name='Период')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Виктория',
                'verbose_name_plural': 'Виктории',
                'ordering': ('-created_at',),
            },
        ),
    ]
