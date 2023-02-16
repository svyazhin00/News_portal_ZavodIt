from django.db import models
from django.urls import reverse



# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    count = models.PositiveIntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    is_published = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'news_id': self.slug})

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('tag_news', kwargs={'tag_slug': self.slug})
