from django.http import HttpResponse
from django.shortcuts import render

from articles.models import Articles, ArticlesCategories


def index(request):
    if not request.COOKIES.get('open_site'):
        response = HttpResponse("Открытие сайта!")
        response.set_cookie('open_site', 'true', max_age=3600)
    categories = ArticlesCategories.objects.filter(is_published=True)
    new_articles = Articles.objects.filter(is_published=True).order_by('-created_at')
    filtered_articles = []
    for article in new_articles:
        if article.category and not article.category.is_published:
            continue
        if article.subcategory and not article.subcategory.is_published:
            continue
        filtered_articles.append(article)
    new_articles = filtered_articles[:3]
    return render(request, 'homepage/index.html', {'categories': categories, 'new_articles': new_articles})
