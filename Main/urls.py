from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/<slug:blog_slug>', views.blog, name='blog'),
    path('blogs/', views.blogs, name='blogs'),
]