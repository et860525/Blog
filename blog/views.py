from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, Permission, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


from .filter import PostsFilter
from .models import Post, Tag
from .forms import *

# Create your views here.
#def home(request):
#    posts = Post.objects.filter(activate=True, featured=True)[:3]
#
#    context = {'posts': posts}
#    return render(request, 'blog/home.html', context)

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

# Sign in
def signInView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'blog/signIn.html', {})

# Sign out
def signOutView(request):
    logout(request)
    return redirect('signIn')

# Register
def registerView(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=form.cleaned_data['username'])
            group = Group.objects.get(name='Users')
            user.groups.add(group)
            return redirect('signIn')

    context = {'form': form}
    return render(request, 'blog/register.html', context)


# CRUD
@login_required(login_url='home')
def create_post(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'blog/form_post.html', context)

@login_required(login_url='home')
def update_post(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'blog/form_post.html', context)

@login_required(login_url='home')
def delete_post(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == "POST":
        post.delete()
        return redirect('home')

    context = {'post': post}
    return render(request, 'blog/delete_post.html', context)