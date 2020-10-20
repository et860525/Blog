from django import forms
from django.forms import ModelForm

from .models import Post

class PostForm(ModelForm):
    class Meta():
        model = Post
        exclude = ('modified',)
    
class ContactForm(ModelForm):
    name = forms.CharField(max_length=225)
    email = forms.EmailField()
    body = forms.Textarea()
