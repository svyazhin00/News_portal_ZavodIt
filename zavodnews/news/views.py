import json

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.generic import *
from rest_framework import generics, mixins
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import *


from .models import News, Tag
from serializers import NewsSerializer


def home_view(request):
    """Функция для выгрузки главной страницы"""
    return render(request, 'news/all_news.html')


class NewsListApiView(generics.ListCreateAPIView):
    """Класс получения списка всех новостей"""
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    # permission_classes = [IsAuthenticated, ]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)
        response_data = {'response': response.data}
        response.data = response_data
        return response


def current_news(request, **kwargs):
    """Функция для выгрузки конкретной новости"""
    return render(request, 'news/some_news.html')


class NewsApiView(RetrieveUpdateDestroyAPIView, ListCreateAPIView):
    """Класс представления конретной новости"""
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def get(self, request, *args, **kwargs):
        question = get_object_or_404(News, slug=kwargs['slug'])
        question.count_view += 1
        question.save()
        serializer = NewsSerializer(question).data
        return self.retrieve(request, *args, **kwargs)

    def get_object(self, **kwargs):
        queryset = self.get_queryset()
        obj = get_object_or_404(News, slug=self.kwargs['slug'])
        self.check_object_permissions(self.request, obj)
        return obj

    # def patch(self, request, *args, **kwargs):
    #     post = News.objects.get(slug=self.kwargs['slug'])
    #     user = User.objects.get(username=request.user)
    #
    #     if list(request.data.keys())[0] == 'dislike':
    #         post_dislike_user_list = post.user_dislikes.all()
    #         if user in post_dislike_user_list:
    #             post.dislike -= 1
    #             post.user_dislikes.remove(user)
    #         else:
    #             post.dislike += 1
    #             post.user_dislikes.add(user)
    #     else:
    #         post_like_user_list = post.user_likes.all()
    #         if user in post_like_user_list:
    #             post.likes -= 1
    #             post.user_likes.remove(user)
    #         else:
    #             post.likes += 1
    #             post.user_likes.add(user)
    #     post.save()
    #     print(post.dislike, post.likes)
    #
    #     return self.partial_update(request, *args, **kwargs)


class LikeNewsApiView(RetrieveUpdateDestroyAPIView):
    """Класс для лайка поста"""
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def get(self, request, *args, **kwargs):
        post = News.objects.get(slug=self.kwargs['slug'])
        user = User.objects.get(username=request.user)
        post_like_user_list = post.user_likes.all()
        if user in post_like_user_list:
            post.likes -= 1
            post.user_likes.remove(user)
        else:
            post.likes += 1
            post.user_likes.add(user)
        post.save()
        serializer = NewsSerializer(post).data
        return self.retrieve(request, *args, **kwargs)

    def get_object(self, **kwargs):
        queryset = self.get_queryset()
        obj = get_object_or_404(News, slug=self.kwargs['slug'])
        self.check_object_permissions(self.request, obj)
        return obj

class DislikeNewsApiView(RetrieveUpdateDestroyAPIView):
    """Класс для дизлайка поста"""
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def get(self, request, *args, **kwargs):
        post = News.objects.get(slug=self.kwargs['slug'])
        user = User.objects.get(username=request.user)
        post_dislike_user_list = post.user_dislikes.all()
        if user in post_dislike_user_list:
            post.dislike -= 1
            post.user_dislikes.remove(user)
        else:
            post.dislike += 1
            post.user_dislikes.add(user)
        post.save()
        serializer = NewsSerializer(post).data
        return self.retrieve(request, *args, **kwargs)

    def get_object(self, **kwargs):
        queryset = self.get_queryset()
        obj = get_object_or_404(News, slug=self.kwargs['slug'])
        self.check_object_permissions(self.request, obj)
        return obj

class Search(ListAPIView):
    """Класс представления новостей по конкретному тегу"""
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.filter(tags__slug=self.kwargs['slug'])

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)
        response_data = {'response': response.data}
        response.data = response_data
        return response


def statistics(request):
    """Функция для выгрузки cтраницы статистики"""
    return render(request, 'news/statistic.html')


class StatisticsApiView(generics.ListCreateAPIView):
    """ Класс представления отсортированного списка новостей"""

    queryset = News.objects.all().order_by("-count_view")
    serializer_class = NewsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)
        response_data = {'response': response.data}
        response.data = response_data
        return response

def login(request):
    """Функция для выгрузки конкретной новости"""
    return render(request, 'news/login.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
