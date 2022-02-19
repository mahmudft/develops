from celery import shared_task
from .models import Post


@shared_task
def delete_upvotes():
    posts = Post.objects.all()
    for post in posts:
        post.upvotes = 0
        post.save()