from django.shortcuts import get_object_or_404, HttpResponseRedirect, render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Blog
from .forms import BlogForm, CommentForm


def search_blogs(request, blogs):
    """
    A function to search blogs based on user input.
    It accepts a request and a queryset of blogs,
    and returns a filtered queryset.
    """
    query = request.GET.get('q')

    if query:
        queries = Q(title__icontains=query) | Q(
            author__username__icontains=query) | Q(
            interests__name__icontains=query)
        blogs = blogs.filter(queries)

        if not blogs.exists():
            messages.warning(request, f"No results found for '{query}'.")
        else:
            messages.success(request, f"blogs found for '{query}'.")

    return blogs


@login_required
def create_blog(request):
    """
    A view to create a blog
    """
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            author = request.user if request.user.is_authenticated else None
            form.save(commit=True, author=author)
            messages.success(request, 'Successfully created blog!')
            return redirect('blog_list')
        else:
            messages.error(request, 'Failed to create blog. \
            Please ensure the form is valid.')
    else:
        form = BlogForm()

    return render(request, 'blog/create_blog.html', {'form': form})


@login_required
def blog_list(request):
    """
    A view to render all the blogs on the blog page
    """
    blogs = Blog.objects.all()

    if request.GET:
        blogs = search_blogs(request, blogs)

    return render(request, 'blog/blog_list.html', {'blogs': blogs})


@login_required
def blog_detail(request, blog_id):
    """
    A view to show an individual blog details
    """
    queryset = Blog.objects.all()
    blog = get_object_or_404(queryset, pk=blog_id)
    comments = blog.comments.filter(approved=True).order_by('created_on')
    liked = False

    if request.user.is_authenticated and blog.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.blog = blog
            comment.save()
            messages.success(request, 'Comment submitted! Please wait for approval.')
            return redirect('blog_detail', blog_id=blog_id)
        else:
            comment_form = CommentForm()
            messages.error(request,
                           'Update failed. Please ensure the form is valid.')
    else:
        comment_form = CommentForm()

    context = {
        'blog': blog,
        'comments': comments,
        'commented': request.method == 'POST',
        'liked': liked,
        'comment_form': comment_form,
        'blog_id': blog_id
    }
    return render(request, 'blog/blog_detail.html', context)


@login_required
def edit_blog(request, blog_id):
    """Edit a blog you created"""

    blog = get_object_or_404(Blog, pk=blog_id)

    if blog.author != request.user:
        return render(request, 'blog/unauthorized_access.html')

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog Editted!')
            return redirect('blog_list')
        else:
            messages.error(request, 'Failed to edit blog.\
            Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blog/edit_blog.html', {'form': form, 'blog': blog})


@login_required
def delete_blog(request, blog_id):
    """Delete a blog you created"""
    blog = get_object_or_404(Blog, pk=blog_id)

    if blog.author != request.user:
        return render(request, 'blog/unauthorized_access.html')

    if request.method == 'POST':
        blog.delete()
        messages.success(request, 'Product deleted!')
        return redirect('blog_list')

    return render(request, 'blog/delete_blog.html', {'blog': blog})


@login_required
def blog_like(request, blog_id):
    """Like other blogs"""
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == 'POST':
        if blog.likes.filter(id=request.user.id).exists():
            blog.likes.remove(request.user)
        else:
            blog.likes.add(request.user)

    return HttpResponseRedirect(reverse('blog_detail', args=[blog_id]))
