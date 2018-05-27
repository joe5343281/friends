from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

import random, string

from posts.models import Post, PostForm

def show_posts_url():
    posts = Post.objects.all()
    return posts 

def show_post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')

@login_required
def editor(request):
    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = request.user.username
            slug = ''.join(random.choice(string.ascii_letters + \
                           string.digits) for x in range(10))
            body = form.cleaned_data['body']
            pub_date = timezone.now()

            post = Post.objects.create(title=title, author=author, slug=slug, body=body, pub_date=pub_date)
            return redirect(f'/post/{slug}')
    
    form = PostForm()
    return render(request, 'editor.html', locals())

@login_required
def myPosts(request):
    posts = Post.objects.filter(author=request.user.username)
    return render(request, 'myposts.html', locals())

@login_required
def modifyPost(request, slug):
    
    post = Post.objects.get(slug=slug)
    if request.user.username is not post.author:
        return redirect(f"/post/{{post.slug}}")

    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            post.title = title
            post.body = body
            post.save()
            return redirect(f'/post/{post.slug}')

    form = PostForm({'title': post.title, 'body': post.body})
    return render(request, 'editor.html', {'form': form})

@login_required
def deletePost(request, slug): 
    post = Post.objects.get(slug=slug)
    if request.user.username is post.author:
        post.delete()
    return redirect('/')
