from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from news.models import *

menu = [{'title':'Новости', 'url_name': 'main'},
        {'title':'Популярные новости', 'url_name':'popular'},
        {'title':'Поиск по тегу', 'url_name':'research'}
        ]


# гланвая страница со всеми новостями
def start_app(request):
    posts = News.objects.all()
    tags = Tag.objects.all()

    context = {
        'posts': posts,
        'tags': tags,
        'menu': menu,
        'title': 'Свежие новости!'
    }
    return render(request, 'news/all_news.html', context=context)

def popular_news(request):
    return render(request, 'news/popular_news.html', {'menu': menu, 'title': 'Популярные новости!'})

def research(request):
    return render(request, 'news/research.html', {'menu': menu, 'title': 'Поиск!'})

#функция представления конкретного поста
def some_news(request, news_id):
    post = get_object_or_404(News, slug=news_id)
    context = {
        'post': post,
        'tags': post.tags,
        'menu': menu,
        'title': post.title,
    }
    return render(request, 'news/some_news.html', context=context)

#функция представления списка постов по конкретному тегу
def tag_news(request, tag_slug):

    tag = get_object_or_404(Tag, slug=tag_slug)

    context = {
        'tag': tag,
        'menu': menu,
        'title': tag.title
    }
    return render(request, 'news/news_tag.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
