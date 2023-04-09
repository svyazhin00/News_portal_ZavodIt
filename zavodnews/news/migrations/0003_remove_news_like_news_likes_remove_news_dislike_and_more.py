# Generated by Django 4.1.7 on 2023-04-07 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_count_news_count_view_news_dislike_news_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='like',
        ),
        migrations.AddField(
            model_name='news',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='news',
            name='dislike',
        ),
        migrations.AddField(
            model_name='news',
            name='dislike',
            field=models.PositiveIntegerField(default=0),
        ),
    ]