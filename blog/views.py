# from django.http import Http404
from django.shortcuts import render
from .models import Post


# Create your views here.
def post_view(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})
