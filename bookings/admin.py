from django.contrib import admin

from .models import Booking, BookingMessage, Review, SkillRequest, SkillRequestApplication


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("listing", "learner", "tutor", "requested_time", "status", "created_at")
    list_filter = ("status", "requested_time", "created_at")
    search_fields = ("listing__title", "learner__username", "tutor__username")


@admin.register(BookingMessage)
class BookingMessageAdmin(admin.ModelAdmin):
    list_display = ("booking", "sender", "created_at")
    search_fields = ("body", "sender__username", "booking__listing__title")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("booking", "reviewer", "tutor", "rating", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("comment", "reviewer__username", "tutor__username")


@admin.register(SkillRequest)
class SkillRequestAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "learner", "status", "created_at")
    list_filter = ("category", "status", "created_at")
    search_fields = ("title", "description", "learner__username")


@admin.register(SkillRequestApplication)
class SkillRequestApplicationAdmin(admin.ModelAdmin):
    list_display = ("skill_request", "tutor", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("skill_request__title", "tutor__username", "pitch")
