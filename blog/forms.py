from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post

class PostForm(ModelForm):
    class Meta():
        model = Post
        exclude = ('modified',)
    
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Username"
    )

    email = forms.EmailField(
        label="Email"
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput()
    )

    password2 = forms.CharField(
        label="Password Check",
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

