from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        """ Meta class for Category model """
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

# Choice Fields
EVENT_TYPES = (
    ("face_to_face", "Face to Face"),
    ("hybrid_event", "Hybrid Event"),
    ("virtual_event", "Virtual Event"),
)


class GetTogether(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50, blank=True, null=True, choices=EVENT_TYPES, default="face_to_face")
    organizer = models.ForeignKey(User, related_name='organized_get_togethers', on_delete=models.CASCADE)
    description = RichTextField(max_length=500, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    image = ResizedImageField(size=[300, None],
                              quality=75, upload_to='get_together/',
                              force_format='WEBP', blank=True)
    image_alt = models.CharField(max_length=100, null=True, blank=True, default='event_image')

    participants = models.ManyToManyField(User, related_name='joined_get_togethers', blank=True)
    max_participants = models.PositiveIntegerField(default=10)
    signup_deadline = models.DateTimeField()

    def is_full(self):
        return self.participants.count() >= self.max_participants

    def __str__(self):
        return self.title
