from django.shortcuts import render, HttpResponse
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import *
from users.models import *
# Create your views here.
# def index(request):
#     return HttpResponse("Hello World!")

def index(request):
    context={
        'posts':Post.objects.order_by('-date_posted')[:6]
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

def categories(request):
    context={
        'posts':Post.objects.all()[:6],
        'users':Profile.objects.all()
    }
    return render(request, 'blog/categories.html',context)

def allposts(request):
    context={
        'posts':Post.objects.order_by('date_posted')
    }
    return render(request, 'blog/allposts.html',context)



from django.urls import reverse_lazy
class PostCreateView( CreateView):
    model = Post
    template_name = 'blog/contest-detail.html'
    fields = ['title','image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    success_url = reverse_lazy('index')