from datetime import timedelta
import secrets

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    listed_skills = models.CharField(max_length=255, blank=True)
    reset_otp = models.CharField(max_length=6, blank=True)
    reset_otp_expires_at = models.DateTimeField(null=True, blank=True)

    def create_reset_otp(self):
        self.reset_otp = f"{secrets.randbelow(1000000):06d}"
        self.reset_otp_expires_at = timezone.now() + timedelta(minutes=10)
        self.save(update_fields=["reset_otp", "reset_otp_expires_at"])
        return self.reset_otp

    def clear_reset_otp(self):
        self.reset_otp = ""
        self.reset_otp_expires_at = None
        self.save(update_fields=["reset_otp", "reset_otp_expires_at"])

    def otp_is_valid(self, otp):
        return (
            self.reset_otp == otp
            and self.reset_otp_expires_at is not None
            and timezone.now() <= self.reset_otp_expires_at
        )
