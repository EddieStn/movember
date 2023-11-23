from django import forms
from .models import Category, GetTogether


class GetTogetherForm(forms.ModelForm):
    class Meta:
        model = GetTogether
        fields = ['title', 'category', 'description', 'date', 'time', 'location', 'max_participants', 'signup_deadline', 'image', 'image_alt']
