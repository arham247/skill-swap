from django.contrib import admin

from .models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "tutor", "availability", "is_public", "created_at")
    list_filter = ("category", "is_public", "created_at")
    search_fields = ("title", "description", "tutor__username", "tutor__email")
