"""friends URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from mainsite.views import home
from chat.views import chat
from posts.views import show_post, editor, modifyPost, deletePost, myPosts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=home, name='home'),
    path('accounts/', include('mainsite.urls')),
    path('post/<str:slug>/', view=show_post),
    path('chat/', view=chat, name='chat'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('editor/', view=editor, name='editor'),
    path('editor/<str:slug>/', view=modifyPost),
    path('delete/<str:slug>/', view=deletePost),
    path('myposts/', view=myPosts, name='myPosts')
]
