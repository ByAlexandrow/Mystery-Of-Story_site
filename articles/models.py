from django.db import models
from django.contrib.auth import get_user_model

from tinymce.models import HTMLField


User = get_user_model()


class ArticlesCategories(models.Model):
    articles_category_title = models.CharField(
        max_length=40,
        verbose_name='Категория',
    )
    articles_category_img = models.ImageField(
        upload_to='image/articles_category/',
        verbose_name='Титульная картинка категории',
    )
    articles_category_description = models.CharField(
        max_length=100,
        verbose_name='Описание',
        default='Описание категории',
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовать',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.articles_category_title


class ArticlesSubcategories(models.Model):
    articles_subcategory_title = models.CharField(
        max_length=40,
        verbose_name='Подкатегория',
    )
    articles_subcategory_img = models.ImageField(
        upload_to='image/articles_category/',
        verbose_name='Титульная картинка подкатегории',
    )
    articles_subcategory_description = models.CharField(
        max_length=100,
        verbose_name='Описание',
        default='Описание подкатегории',
    )
    category = models.ForeignKey(
        ArticlesCategories,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        default='2',
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовать',
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегория'
    
    def __str__(self):
        return self.articles_subcategory_title


class Articles(models.Model):
    articles_title = models.CharField(
        max_length=30,
        verbose_name='Название статьи',
    )
    articles_title_img = models.ImageField(
        upload_to='image/articles_img/',
        verbose_name='Титульная картинка',
    )
    articles_description = models.CharField(
        max_length=50,
        default='Описание статьи для титульной страницы!',
        verbose_name='Описание статьи',
    )
    articles_text_1 = HTMLField(
        default=(
            f'Текст статьи. 1 отступ. 100-130 слов. Шрифт: заголовки - 18, подзаголовки - 14, текст - 12, белый цвет.'
        ),
        verbose_name='Текст статьи 1 (left)',
        blank=True,
    )
    article_img_1 = models.ImageField(
        upload_to='image/articles_description_img/',
        verbose_name='Картинка 1',
        blank=True,
        null=True,
    )
    articles_text_2 = HTMLField(
        default=(
            f'Текст статьи. 1 отступ. Строка. Шрифт: заголовки - 18, подзаголовки - 14, текст - 12, белый цвет.'
        ),
        verbose_name='Текст статьи 2 (string)',
        blank=True,
    )
    articles_text_3 = HTMLField(
        default=(
            f'Текст статьи. 1 отступ. 100-130 слов. Шрифт: заголовки - 18, подзаголовки - 14, текст - 12, белый цвет.'
        ),
        verbose_name='Текст статьи 3 (right)',
        blank=True,
    )
    article_img_2 = models.ImageField(
        upload_to='image/articles_description_img/',
        verbose_name='Картинка 2',
        blank=True,
        null=True,
    )
    articles_text_4 = HTMLField(
        default=(
            f'Текст статьи. 1 отступ. Строка. Шрифт: заголовки - 18, подзаголовки - 14, текст - 12, белый цвет.'
        ),
        verbose_name='Текст статьи 4 (string)',
        blank=True,
    )
    articles_text_5 = HTMLField(
        default=(
            f'Текст статьи. 1 отступ. 100-130 слов. Шрифт: заголовки - 18, подзаголовки - 14, текст - 12, белый цвет.'
        ),
        verbose_name='Текст статьи 5 (left)',
        blank=True,
    )
    category = models.ForeignKey(
        ArticlesCategories,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Категория'
    )
    subcategory = models.ForeignKey(
        ArticlesSubcategories,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Подкатегория',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Автор'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовать'
    )

    def __str__(self):
        return self.articles_title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class ArticlesImage(models.Model):
    about_us = models.ForeignKey(
        Articles,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name='Статья',
    )
    images = models.ImageField(
        upload_to='image/articles_carousel/',
        verbose_name='Карусель картинок',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f'{self.images.name}'
