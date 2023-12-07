from django.urls import path
<<<<<<< HEAD
from .views import PostListView, PostDetailView

urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="blog_detail"),
=======
from blog import views

urlpatterns = [
    # path('posts/', views.post_view, name='post_index'),
>>>>>>> 1d6145c53db21e8bc17c72aafa7c9796ba0bd4b4
]
