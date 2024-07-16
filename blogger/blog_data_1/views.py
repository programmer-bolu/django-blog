from django.shortcuts import render
from . import models
# Create your views here.

def home(request):
    posts = models.Post.objects.all()
    return render(request, 'index.html', {'posts': posts})