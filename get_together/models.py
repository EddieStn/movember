from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GetTogether(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, blank=False, null=False, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='get_together_images/', blank=True, null=True)
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    organizer = models.ForeignKey(User, related_name='organized_get_togethers', on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='joined_get_togethers', blank=True)
    max_participants = models.PositiveIntegerField(default=10)
    signup_deadline = models.DateTimeField()

    def is_full(self):
        return self.participants.count() >= self.max_participants

    def __str__(self):
        return self.title
