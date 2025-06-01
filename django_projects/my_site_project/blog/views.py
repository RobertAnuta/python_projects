from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post

all_posts = Post.objects.all().order_by("-date")


def get_date(post):
    return post["date"]


def index(request):
    latest_post = Post.objects.all().order_by("-date")[:3]

    return render(
        request,
        "blog/index.html",
        {
            "posts": latest_post,
        },
    )


def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_details(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(
        request,
        "blog/post-details.html",
        {
            "post": identified_post,
        },
    )
