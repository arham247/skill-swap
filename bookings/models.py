from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

from listings.models import Listing


class Booking(models.Model):
    STATUS_PENDING = "pending"
    STATUS_ACCEPTED = "accepted"
    STATUS_REJECTED = "rejected"
    STATUS_COMPLETED = "completed"
    STATUS_CANCELLED = "cancelled"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_ACCEPTED, "Accepted"),
        (STATUS_REJECTED, "Rejected"),
        (STATUS_COMPLETED, "Completed"),
        (STATUS_CANCELLED, "Cancelled"),
    ]
    ACTIVE_STATUSES = (STATUS_PENDING, STATUS_ACCEPTED)

    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bookings")
    learner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="learner_bookings",
    )
    tutor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tutor_bookings",
    )
    requested_time = models.DateTimeField()
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.listing.title} booking for {self.learner}"

    def get_absolute_url(self):
        return reverse("booking_detail", args=[self.pk])

    @property
    def can_message(self):
        return self.status in {self.STATUS_ACCEPTED, self.STATUS_COMPLETED}


class BookingMessage(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Message from {self.sender} on booking {self.booking_id}"


class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name="review")
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews_given",
    )
    tutor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews_received",
    )
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.rating}/5 review for {self.tutor}"


class SkillRequest(models.Model):
    STATUS_OPEN = "open"
    STATUS_FULFILLED = "fulfilled"
    STATUS_CANCELLED = "cancelled"

    STATUS_CHOICES = [
        (STATUS_OPEN, "Open"),
        (STATUS_FULFILLED, "Fulfilled"),
        (STATUS_CANCELLED, "Cancelled"),
    ]

    learner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="skill_requests",
    )
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=30, choices=Listing.CATEGORY_CHOICES)
    description = models.TextField()
    availability = models.CharField(max_length=150)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_OPEN)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("skill_request_detail", args=[self.pk])


class SkillRequestApplication(models.Model):
    STATUS_PENDING = "pending"
    STATUS_ACCEPTED = "accepted"
    STATUS_REJECTED = "rejected"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_ACCEPTED, "Accepted"),
        (STATUS_REJECTED, "Rejected"),
    ]

    skill_request = models.ForeignKey(
        SkillRequest,
        on_delete=models.CASCADE,
        related_name="applications",
    )
    tutor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="skill_request_applications",
    )
    pitch = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    booking = models.OneToOneField(
        Booking,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="skill_request_application",
    )

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["skill_request", "tutor"],
                name="unique_application_per_tutor_request",
            )
        ]

    def __str__(self):
        return f"{self.tutor} application for {self.skill_request}"
