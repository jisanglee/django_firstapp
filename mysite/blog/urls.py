from django.urls import path
from . import views

urlpatterns = [
    #all post
    path('', views.post_list, name='post_list'),
    #one post
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #new post
    path('post/new', views.post_new, name='post_new'),
    #edit post
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
