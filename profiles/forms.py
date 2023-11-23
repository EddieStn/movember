from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['alias', 'image', 'about_me', 'is_facilitator', 'show_alias']
