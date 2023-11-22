from django.contrib import admin
from .models import Blog, Interest

class InterestInline(admin.TabularInline):
    model = Blog.interests.through
    extra = 1
    min_num = 0
    def get_max_num(self, request, obj=None, **kwargs):
        return None

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'created_at', 'likes_count', 'comments_count')
    search_fields = ['title', 'content', 'author__username']
    date_hierarchy = 'created_at'
    inlines = [InterestInline]

    def display_author(self, obj):
        return obj.author.username if obj.author else "Anonymous User"

    display_author.short_description = 'Author'
    display_author.admin_order_field = 'author__username'

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
