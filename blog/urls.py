from django.urls import path

from blog import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.posts, name='home'),
    path('post/<slug:slug>', views.post, name='post'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Sign in and Sign out
    path('signin/', views.signInView, name='signIn'),
    path('signout/', views.signOutView, name='signOut'),

    # register
    path('register/', views.registerView, name='register'),

    # CRUD
    path('create_post/', views.create_post, name='create_post'),
    path('update_post/<slug:slug>', views.update_post, name='update_post'),
    path('delete_post/<slug:slug>', views.delete_post, name='delete_post'),
]

