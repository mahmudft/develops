from django.db import models

# Create your models here.


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=400)
    link = models.URLField()
    creation_date = models.DateField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=700)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.IntegerField()
    author_name = models.CharField(max_length=700)
    content = models.CharField(max_length=500)
    creation_date = models.DateField(auto_now_add=True)
