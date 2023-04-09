from rest_framework import serializers

from news.models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title', 'slug')


class NewsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'count_view', 'tags', 'likes', 'dislike', 'slug', 'photo')
