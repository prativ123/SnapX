from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
# def index(request):
#     return HttpResponse("Hello World!")

def index(request):
    context={
        'posts':Post.objects.all()[:6]
    }
    return render(request, 'blog/index.html',context)

def contests(request):
    posts=Post.objects.all()[:6]
    for post in posts:
        post.rank = post.id + 5
    context={
        'posts':posts
    }
    
    return render(request, 'blog/contests.html',context)