""" User Profile Model """

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField


class Profile(models.Model):
    """
    A model to create and manage user profiles
    """
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    alias = models.CharField(max_length=100, blank=True)
    image = ResizedImageField(size=[100, 200],
                              quality=75, upload_to='profiles/',
                              force_format='WEBP', blank=True)
    about_me = RichTextField(max_length=280, null=True, blank=True)
    is_facilitator = models.BooleanField(default=False)
    show_alias = models.BooleanField(default=True)

    def __str__(self):
        return str(self.alias) if self.alias else str(self.user.username)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create or update the user profile """
    if created:
        Profile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.profile.save()
