from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('create_blog/', views.create_blog, name='create_blog'),
]