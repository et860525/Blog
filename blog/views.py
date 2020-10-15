from django.shortcuts import render, redirect

from .models import Post, Tag
from .forms import PostForm

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

def create_post(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts')

    context = {'form': form}
    return render(request, 'blog/form_post.html', context)