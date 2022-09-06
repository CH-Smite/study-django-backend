from django.shortcuts import render
from . models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by("-pk")

    return render(
        request,
        "blog/index.html",
        {
            "posts": posts,
        }
    )

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        "blog/post_detail.html",
        {
            "post":post,
        }
    )