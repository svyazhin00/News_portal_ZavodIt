from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import *

from news.models import *
from news.utils import *


# главная страница со всеми новостями
class StartApp(DataMixin, ListView):
    posts = News
    template_name = 'news/all_news.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return News.objects.all()


#функция представления конкретного поста
class NewPost(DataMixin, DetailView):
    post = News
    template_name = 'news/some_news.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])

        if context:
            context['object'].count += 1
            context['object'].save()
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return News.objects.filter(slug=self.kwargs['post_slug'])


#Класс отображения постов по конкретному тегу
class TagNews(DataMixin, ListView):
    posts = News
    template_name = 'news/all_news.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_title = Tag.objects.filter(slug=self.kwargs['tag_slug'])
        c_def = self.get_user_context(title='Новости - ' + str(tag_title[0].title))
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return News.objects.filter(tags__slug=self.kwargs['tag_slug'])

class Search(DataMixin, ListView):
    posts = News
    template_name = 'news/all_news.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        c_def = self.get_user_context(title='Новости')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return News.objects.filter(tags__title__icontains=self.request.GET.get('search'))


def popular_news(request):
    posts = News.objects.order_by('-count')
    context = {
        'posts': posts,
        'menu': menu,
    }
    return render(request, 'news/popular_news.html', context=context)



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
