from django import forms
from .models import Category, GetTogether


class GetTogetherForm(forms.ModelForm):

    new_category = forms.CharField(max_length=100, required=False, help_text="This will be a new category.")
    class Meta:
        model = GetTogether
        fields = ['title', 'category', 'new_category', 'description', 'date', 'time', 'location', 'max_participants', 'signup_deadline', 'image', 'image_alt']

    def __init__(self, *args, **kwargs):
        super(GetTogetherForm, self).__init__(*args, **kwargs)
        self.fields['image_alt'].required = True
