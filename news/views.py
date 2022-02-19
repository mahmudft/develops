from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from news.models import Post, Comment
from news.serializers import PostSerializer, CommentSerializer

# Create your views here.


@api_view(["GET", "POST"])
def posts_list_create(request):
    """
    Returns all of Posts
    """
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        print(request.data)
        serializer = PostSerializer(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE", "PUT"])
def post_delete_update(request, pk):
    print(pk)
    if request.method == "DELETE":
        data = Post.objects.get(id=pk)
        data.delete()
        return Response(status=200)

    if request.method == "PUT":
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(data=serializer.errors)


@api_view(["GET", "POST"])
def comment_list_create(request, pk):
    if request.method == "GET":
        post = Post.objects.get(id=pk)
        if post:
            comments = Comment.objects.filter(post_id=pk)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        else:
            return Response(status=404)
    if request.method == "POST":
        serializer = CommentSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(post_id=pk)
            return Response(serializer.data)
        else:
            return Response(data=serializer.errors)


@api_view(["DELETE", "PUT"])
def comment_delete_update(request, pk, comment_id):
    if request.method == "DELETE":
        post = Post.objects.get(id=pk)
        if post:
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        post = Post.objects.get(id=pk)
        if post:
            comment = Comment.objects.get(id=comment_id)
            serializer = CommentSerializer(
                instance=comment, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def upvote(request, pk):
    post = Post.objects.get(id=pk)

    if post:
        post.upvotes += 1
        post.save()
        return Response(status=status.HTTP_200_OK)
    else: 
        return Response(status=status.HTTP_400_BAD_REQUEST)