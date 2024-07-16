from django.shortcuts import render, get_list_or_404
from . import models
# Create your views here.

def home(request):
    posts = models.Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def blogpost(request, id):
    post = get_list_or_404(models.Post, id=id)
    return render(request, 'blog.html', {'post': post})