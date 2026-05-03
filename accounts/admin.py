from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = DjangoUserAdmin.fieldsets + (
        ("Profile", {"fields": ("bio", "listed_skills", "reset_otp", "reset_otp_expires_at")}),
    )
    add_fieldsets = DjangoUserAdmin.add_fieldsets + (
        ("Profile", {"fields": ("email", "bio", "listed_skills")}),
    )
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
