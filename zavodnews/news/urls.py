from django.urls import path

from .views import *

urlpatterns = [

    path('news/', start_app,name='main'),
    path('news/most_popular/', popular_news, name='popular'),
    path('news/research/', research, name='research'),
    path('post/<slug:news_id>/', some_news, name='post'),
    path('tag/<slug:tag_slug>/', tag_news, name='tag_news'),
]