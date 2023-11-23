from django import forms
from .models import Blog, Interest


class BlogForm(forms.ModelForm):
    interests = forms.CharField(
        max_length=255,
        required=False,
        help_text='Enter interests separated by commas',
    )

    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']

    def save(self, commit=True, author=None):
        blog = super().save(commit=False)

        if author is not None:
            blog.author = author

        if commit:
            blog.save()

        interest_names = [name.strip() for name in self.cleaned_data['interests'].split(',')]
        for name in interest_names:
            interest, created = Interest.objects.get_or_create(name=name)
            blog.interests.add(interest)

        return blog
