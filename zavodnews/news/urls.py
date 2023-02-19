from django.urls import path

from .views import *

urlpatterns = [

    path('news/', StartApp.as_view(),name='main'),
    path('news/most_popular/', popular_news, name='popular'),
    path('news/search/', Search.as_view(), name='search'),
    path('post/<slug:post_slug>/', NewPost.as_view(), name='post'),
    path('tag/<slug:tag_slug>/', TagNews.as_view(), name='tag_news'),

]