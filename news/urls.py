from django.urls import path
from . import views

urlpatterns = [
    path("", views.posts_list_create, name="post_list"),
    path("<int:pk>", views.post_delete_update, name="posts_del"),
    path("<int:pk>/comments", views.comment_list_create, name="comment_crt"),
    path(
        "<int:pk>/comments/<int:comment_id>",
        views.comment_delete_update,
        name="comment_delete_update",
    ),
    path("<int:pk>/upvote", views.upvote, name="upvote"),
]
