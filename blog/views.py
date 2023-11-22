from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm


@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            author = request.user if request.user.is_authenticated else None
            blog = form.save(commit=True, author=author)
            return redirect('blog_list')
    else:
        form = BlogForm()

    context = {'form': form}
    return render(request, 'blog/create_blog.html', context)


@login_required
def blog_list(request):
    """
    A view to render all the blogs on the blog page
    """
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog/blog_list.html', context)
