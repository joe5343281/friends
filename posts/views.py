from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post

def show_posts_link():
    posts = Post.objects.all()
    return posts 

def show_post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')
