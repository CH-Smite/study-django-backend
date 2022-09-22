from django.shortcuts import render
from django.views.generic import ListView
from . models import Post, Category
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
class PostList(ListView):
    model = Post
    ordering = "-pk"
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context["categories"] = Category.objects.all()
        context["no_category_post_count"] = Post.objects.filter(category=None).count()
        return context

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        "blog/post_detail.html",
        {
            "post":post,
        }
    )
