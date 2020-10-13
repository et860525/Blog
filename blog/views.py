from django.shortcuts import render

from .models import Post, Tag

# Create your views here.
def home(request):
    return render(request, 'blog/home.html', {})

def posts(request):
    posts = Post.objects.filter(activate=True)

    context = {'posts': posts}
    return render(request, 'blog/posts.html', context)

def post(request, slug):
    post = Post.objects.get(slug=slug)

    context = {'post': post}
    return render(request, 'blog/post.html', context)

def about(request):
    return render(request, 'blog/about.html', {})

def contact(request):
    return render(request, 'blog/contact.html', {})
