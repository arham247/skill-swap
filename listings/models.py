from django.db import models
from django.urls import reverse


class Listing(models.Model):
    CATEGORY_CHOICES = [
        ("programming", "Programming"),
        ("design", "Design"),
        ("language", "Language"),
        ("business", "Business"),
        ("other", "Other"),
    ]

    tutor = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="listings",
    )
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    description = models.TextField()
    availability = models.CharField(max_length=150)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("listing_detail", args=[self.pk])
