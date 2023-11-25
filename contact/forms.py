from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Contact
from djrichtextfield.widgets import RichTextWidget


class ContactForm(forms.ModelForm):
    """
    Form class for the contact form
    """
    class Meta:
        model = Contact
        fields = [
            'full_name',
            'email',
            'interests',
            'bio',
            'why_you_want_to_become_a_facilitator',
        ]

    bio = forms.CharField(widget=RichTextWidget()),
    why_you_want_to_become_a_facilitator = forms.CharField(widget=RichTextWidget()),

    widget = {
        'bio': forms.Textarea(attrs={"rows": 3}),
        'why_you_want_to_become_a_facilitator': forms.Textarea(attrs={"rows": 3})
    }

    labels = {
        'full_name': 'First Name & Last Name',
        'email': 'Email',
        'interests': 'Interests',
        'bio': 'Tell us about you',
        'why_you_want_to_become_a_facilitator': 'Why do you want to become a facilitator?'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))