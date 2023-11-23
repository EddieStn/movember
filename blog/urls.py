from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
]