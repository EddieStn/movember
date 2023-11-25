from django.contrib import admin
from .models import GetTogether, Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class GetTogetherAdmin(admin.ModelAdmin):
    """" Get Together admin """
    list_display = (
        "pk",
        "title",
        "category",
        "event_type",
        "organizer",
        "description",
        "date",
        "time",
        "location",
        "image",
        "image_alt",
        "participants",
        "max_participants",
        "signup_deadline",
    )

    def participants(self, obj):
        return ", ".join([user.username for user in obj.participants.all()])
    participants.short_description = "Participants"


admin.site.register(Category, CategoryAdmin)
admin.site.register(GetTogether, GetTogetherAdmin)
