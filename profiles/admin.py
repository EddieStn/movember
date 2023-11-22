from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "user",
        "alias",
        "image",
        "image_alt",
        "about_me",
        "is_facilitator",
        "show_alias",
    )


admin.site.register(Profile, ProfileAdmin)
