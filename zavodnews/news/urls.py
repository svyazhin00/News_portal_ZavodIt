from django.conf.urls.static import static
from django.urls import path, include, re_path

from zavodnews import settings
from .views import *

urlpatterns = [

    path('statistics/', statistics, name='stat_page'),
    path('api/statistics/', StatisticsApiView.as_view(), name='statistics'),

    path('news/', home_view, name='main'),
    path('api/news/', NewsListApiView.as_view(), name='news'),

    path('news/<slug:slug>/', current_news, name='current_news'),
    path('api/news/<slug:slug>/', NewsApiView.as_view(), name='api_current_news'),
    path('api/like_news/<slug:slug>/', LikeNewsApiView.as_view()),
    path('api/dislike_news/<slug:slug>/', DislikeNewsApiView.as_view()),

    path('api/news/search/<slug:slug>', Search.as_view(), name='search'),

    path('login/', login, name='login_form'),
    path('api/auth/', include('rest_framework.urls')),

    path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),


]