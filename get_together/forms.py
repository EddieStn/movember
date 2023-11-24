from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import GetTogether


class GetTogetherForm(forms.ModelForm):
    """ Form to create a get together event """

    new_category = forms.CharField(max_length=100, required=False,
                                   help_text="This will be a new category.")
    class Meta:
        model = GetTogether
        fields = ['title', 'category', 'new_category', 'event_type',
                  'description', 'date', 'time', 'location', 'max_participants',
                  'signup_deadline', 'image', 'image_alt']

    description = forms.CharField(widget=RichTextWidget())

    widget = {
        'description': forms.Textarea(attrs={"rows": 5}),
    }

    labels = {
        'title': 'Get Together Title',
        'category': 'Event or Interest Category',
        'new_category': 'Add new category only if event or interest is not yet in Categories',
        'description': 'Describe your get together to encourage the community members to join',
        'date': "Date of Get Together",
        'time': 'Time of Get Together',
        'location': 'Location',
        'max_participants': 'Maximum number of participants',
        'signup_deadline': 'Signup Deadline',
        'image': 'Upload an image, if available',
        'image_alt': 'Describe your image to help make it accessible to everyone',
        'event_type': 'Select Event Type',
    }

    def __init__(self, *args, **kwargs):
        super(GetTogetherForm, self).__init__(*args, **kwargs)
        self.fields['image_alt'].required = True
