from django.shortcuts import get_object_or_404, render, redirect
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

    return render(request, 'blog/create_blog.html', {'form': form})


@login_required
def blog_list(request):
    """
    A view to render all the blogs on the blog page
    """
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})


@login_required
def blog_detail(request, blog_id):
    """
    A view to display the blog detail when a user
    clicks on it so they can be able to edit/delete
    """
    blog = get_object_or_404(Blog, pk=blog_id)
    user = request.user

    return render(request, 'blog/blog_detail.html', {'blog': blog, 'user': user})


@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    if blog.author != request.user:
        return render(request, 'blog/unauthorized_access.html')

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blog/edit_blog.html', {'form': form, 'blog': blog})


@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    if blog.author != request.user:
        return render(request, 'blog/unauthorized_access.html')

    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')

    return render(request, 'blog/delete_blog.html', {'blog': blog})