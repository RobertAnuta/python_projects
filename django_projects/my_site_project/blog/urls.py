"""
URL configuration for blog application
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.posts, name="posts-page"),
    path("post/<slug:slug>", views.post_details, name="post-detail-page"),
]
