from django.contrib import admin
from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    filter_horizontal = ['tags', ]
    prepopulated_fields = {'slug': ('title',)}





class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(News, NewsAdmin)
admin.site.register(Tag, TagAdmin)