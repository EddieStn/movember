from django.db import models
from django.contrib.auth.models import User


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Interest(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Like, related_name='blog_likes', blank=True)
    comments = models.ManyToManyField(Comment, related_name='blog_comments', blank=True)
    anonymous = models.BooleanField(default=False)
    interests = models.ManyToManyField(Interest, blank=True)
    image = models.ImageField(upload_to='blog-images/', blank=True, null=True)

    @property
    def likes_count(self):
        return self.likes.count()
    
    @property
    def comments_count(self):
        return self.comments.count()