from django.conf.urls.static import static
from django.urls import path

from zavodnews import settings
from .views import *

urlpatterns = [

    path('statistics/', statistics, name='stat_page'),
    path('api/statistics/', StatisticsApiView.as_view(), name='statistics'),

    path('news/', home_view, name='main'),
    path('api/news/', NewsListApiView.as_view(), name='news'),

    path('news/<slug:slug>/', current_news, name='current_news'),
    path('api/news/<slug:slug>/', NewsApiView.as_view(), name='api_current_news'),


    path('api/news/search/<slug:slug>', Search.as_view(), name='search'),



]