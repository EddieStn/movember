from django.contrib import admin
from .models import Blog, Like, Comment, Interest


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'created_at',
        'author',
        'anonymous',
        'likes_count',
        'comments_count',
    )


admin.site.register(Blog, BlogAdmin)