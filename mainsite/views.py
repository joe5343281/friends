from django.contrib import auth
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login

from posts.views import show_posts_url

def home(request):
	posts = show_posts_url()
	return render_to_response("index.html", locals())

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
