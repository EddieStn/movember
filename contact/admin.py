from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    Admin class for the Contact model.
    """
    list_display = [
        'full_name',
        'email',
        'interests',
        'bio',
        'why_you_want_to_become_a_facilitator',
        'date',
    ]


admin.site.register(Contact, ContactAdmin)