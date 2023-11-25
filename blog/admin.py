from django.contrib import admin
from .models import Interest, Blog, Comment

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'likes_count', 'anonymous',)
    list_filter = ('author', 'created_at', 'anonymous', 'interests',)
    search_fields = ('title', 'author__username',)
    date_hierarchy = 'created_at'
    filter_horizontal = ('interests',)  # To display interests as a horizontal filter

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'blog', 'created_on', 'approved',)
    list_filter = ('blog', 'created_on', 'approved',)
    search_fields = ('name', 'body', 'blog__title',)
    date_hierarchy = 'created_on'
