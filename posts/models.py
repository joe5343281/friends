from django import forms
from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget

class Post(models.Model):    
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = RichTextField()
    pub_date = models.DateTimeField(default=timezone.now)
    
    class Meta:    
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title

class PostForm(forms.Form):
    title = forms.CharField(label = "標題", max_length=200)
    body = forms.CharField(label = "", 
                           widget = CKEditorWidget())
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title
