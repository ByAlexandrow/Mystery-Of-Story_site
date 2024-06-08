# Generated by Django 4.2.13 on 2024-06-08 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('texts', '0006_alter_reactions_reaction_comments_texts_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_text', models.TextField(verbose_name='Текст комментария')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ('created_at',),
            },
        ),
        migrations.RemoveField(
            model_name='texts',
            name='comment',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='texts.texts'),
        ),
    ]
