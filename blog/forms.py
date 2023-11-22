from django import forms
from .models import Blog, Interest


class BlogForm(forms.ModelForm):
    interests = forms.CharField(
        max_length=255, help_text='Enter interests separated by commas'
    )

    class Meta:
        model = Blog
        fields = ['title', 'content', 'anonymous', 'image']

    def save(self, commit=True):
        blog = super().save(commit=False)

        # Save the blog first
        if commit:
            blog.save()

        # Split the interests and create them (if not already exist)
        interest_names = [name.strip() for name in self.cleaned_data['interests'].split(',')]
        for name in interest_names:
            interest, created = Interest.objects.get_or_create(name=name)
            blog.interests.add(interest)

        return blog
