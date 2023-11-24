from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """" User Profile admin """
    list_display = (
        "pk",
        "user",
        "alias",
        "image",
        "about_me",
        "is_facilitator",
        'is_facilitator_approved',
        "show_alias",
    )


admin.site.register(Profile, ProfileAdmin)
