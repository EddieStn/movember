from django.shortcuts import render
from .models import Blog


def blog_list(request):
    """
    A view to render all the blogs on the blog page
    """
    blogs = Blog.objects.all()
    
    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog_list.html', context)
