from rest_framework import serializers
from rest_framework.authtoken.models import Token

from news.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title', 'slug')


class NewsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    user_likes = UserSerializer(many=True, read_only=True)
    user_dislikes = UserSerializer(many=True, read_only=True)

    class Meta:
        model = News
        # fields = ('id', 'title', 'content', 'count_view', 'tags', 'likes', 'dislike', 'slug', 'photo', )
        fields = '__all__'
