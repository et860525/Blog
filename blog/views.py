from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .filter import PostsFilter
from .models import Post, Tag
from .forms import *

# Create your views here.
def home(request):
    posts = Post.objects.filter(activate=True, featured=True)[:3]

    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

def posts(request):
    posts = Post.objects.filter(activate=True).order_by('-created')

    #if 'searchInput' in request.GET:
    #    search_result = request.GET['searchInput']
    #    posts = posts.filter(headline__icontains=search_result)

    post_filter = PostsFilter(request.GET, queryset=posts)
    posts = post_filter.qs

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {'posts': page_obj, 'post_filter': post_filter}
    return render(request, 'blog/posts.html', context)

def post(request, slug):
    post = Post.objects.get(slug=slug)

    context = {'post': post}
    return render(request, 'blog/post.html', context)

def about(request):
    return render(request, 'blog/about.html', {})

def contact(request):
    return render(request, 'blog/contact.html', {})

# CRUD

def create_post(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts')

    context = {'form': form}
    return render(request, 'blog/form_post.html', context)

def update_post(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)

    if request.method == "POST":
        pass

    context = {'form': form}
    return render(request, 'blog/form_post.html', context)

def delete_post(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == "POST":
        pass

    return render(request, 'blog/.html', context)