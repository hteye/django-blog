from .models import Post
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse


class PostListView(ListView):
    template_name = "post_list.html"
    queryset = Post.objects.exclude(published_at__exact=None).order_by("-published_at")[:5]
    context_object_name = "posts"


class PostDetailView(DetailView):
    template_name = "post_detail.html"
    queryset = Post.objects.exclude(published_at__exact=None).order_by("-published_at")
    context_object_name = "post"

    def get_object(self, queryset=None):
        # Override get_object to handle Http404 if the post is not found
        obj = super().get_object(queryset=queryset)
        if obj.published_at is None:
            raise Http404("Post not found")
        return obj