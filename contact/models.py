from django.db import models
from djrichtextfield.models import RichTextField


class Contact(models.Model):
    full_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    interests = models.CharField(max_length=100, null=False, blank=False)
    bio = RichTextField(max_length=150, null=False, blank=False)
    why_you_want_to_become_a_facilitator = RichTextField(max_length=150, null=False, blank=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name

