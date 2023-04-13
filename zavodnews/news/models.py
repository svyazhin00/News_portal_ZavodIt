from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

class News(models.Model):
    user_likes = models.ManyToManyField(User, related_name='likes', blank=True, null=True)
    user_dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
    status_like = models.BooleanField(default=False)
    status_dislike = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, null=True)
    count_view = models.PositiveIntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    is_published = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_news', kwargs={'tag_slug': self.slug})
