from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="blog_detail"),
]
