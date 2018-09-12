from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.template import loader
from .models import Post

# class IndexView():

def index(request):
  # return HttpResponse("Hello World!! このページは投稿ページのindexです。")
  posts =  Post.objects.order_by('-published')
  print(posts)
  return render(request, 'posts/index.html', {'posts': posts})

def detail(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  return render(request, 'posts/detail.html', {'post': post})

def about(request):
  return render(request, 'posts/about.html')

# Create your views here.