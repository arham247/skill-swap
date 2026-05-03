from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from accounts.models import User
from listings.models import Listing

from .models import Booking, BookingMessage, Review, SkillRequest, SkillRequestApplication


class Sprint2WorkflowTests(TestCase):
    def setUp(self):
        self.password = "StrongPass123!"
        self.learner = User.objects.create_user(
            username="learner",
            email="learner@example.com",
            password=self.password,
        )
        self.tutor = User.objects.create_user(
            username="tutor",
            email="tutor@example.com",
            password=self.password,
        )
        self.other = User.objects.create_user(
            username="other",
            email="other@example.com",
            password=self.password,
        )
        self.listing = Listing.objects.create(
            tutor=self.tutor,
            title="Django Sessions",
            category="programming",
            description="Learn Django views and models.",
            availability="Weekends",
        )

    def test_learner_can_request_booking(self):
        self.client.login(username="learner", password=self.password)
        requested_time = timezone.now() + timedelta(days=2)

        response = self.client.post(
            reverse("booking_create", args=[self.listing.pk]),
            {
                "requested_time": requested_time.strftime("%Y-%m-%dT%H:%M"),
                "message": "I want help with class-based views.",
            },
        )

        booking = Booking.objects.get()
        self.assertRedirects(response, reverse("booking_detail", args=[booking.pk]))
        self.assertEqual(booking.learner, self.learner)
        self.assertEqual(booking.tutor, self.tutor)
        self.assertEqual(booking.status, Booking.STATUS_PENDING)

    def test_active_booking_prevents_duplicate_request(self):
        booking = self._create_booking(status=Booking.STATUS_ACCEPTED)
        self.client.login(username="learner", password=self.password)
        requested_time = timezone.now() + timedelta(days=2)

        response = self.client.post(
            reverse("booking_create", args=[self.listing.pk]),
            {
                "requested_time": requested_time.strftime("%Y-%m-%dT%H:%M"),
                "message": "Trying to book the same listing twice.",
            },
        )

        self.assertRedirects(response, reverse("booking_detail", args=[booking.pk]))
        self.assertEqual(Booking.objects.count(), 1)

        response = self.client.get(reverse("listing_detail", args=[self.listing.pk]))
        self.assertContains(response, "View Booking")
        self.assertNotContains(response, "Request Session")

    def test_private_listing_cannot_be_browsed_or_booked(self):
        private_listing = Listing.objects.create(
            tutor=self.tutor,
            title="Private Figma Match",
            category="design",
            description="Internal listing for a fulfilled request.",
            availability="Monday",
            is_public=False,
        )
        self.client.login(username="learner", password=self.password)

        detail_response = self.client.get(reverse("listing_detail", args=[private_listing.pk]))
        booking_response = self.client.get(reverse("booking_create", args=[private_listing.pk]))

        self.assertEqual(detail_response.status_code, 404)
        self.assertEqual(booking_response.status_code, 404)

    def test_tutor_can_accept_booking_and_messages_open(self):
        booking = self._create_booking(status=Booking.STATUS_PENDING)
        self.client.login(username="tutor", password=self.password)

        response = self.client.post(reverse("booking_accept", args=[booking.pk]))

        booking.refresh_from_db()
        self.assertRedirects(response, reverse("booking_detail", args=[booking.pk]))
        self.assertEqual(booking.status, Booking.STATUS_ACCEPTED)

        self.client.post(reverse("booking_detail", args=[booking.pk]), {"body": "Accepted, see you then."})
        self.assertTrue(BookingMessage.objects.filter(booking=booking, sender=self.tutor).exists())

    def test_non_participant_cannot_view_booking(self):
        booking = self._create_booking(status=Booking.STATUS_ACCEPTED)
        self.client.login(username="other", password=self.password)

        response = self.client.get(reverse("booking_detail", args=[booking.pk]))

        self.assertEqual(response.status_code, 403)

    def test_completed_booking_can_be_reviewed_by_learner(self):
        booking = self._create_booking(status=Booking.STATUS_COMPLETED)
        self.client.login(username="learner", password=self.password)

        response = self.client.post(
            reverse("review_create", args=[booking.pk]),
            {"rating": 5, "comment": "Very helpful session."},
        )

        self.assertRedirects(response, reverse("booking_detail", args=[booking.pk]))
        review = Review.objects.get(booking=booking)
        self.assertEqual(review.tutor, self.tutor)
        self.assertEqual(review.reviewer, self.learner)

    def test_skill_request_application_acceptance_creates_booking(self):
        skill_request = SkillRequest.objects.create(
            learner=self.learner,
            title="Need help with SQL",
            category="programming",
            description="Joins and indexing.",
            availability="Monday evening",
        )
        application = SkillRequestApplication.objects.create(
            skill_request=skill_request,
            tutor=self.tutor,
            pitch="I can teach SQL with examples.",
        )
        self.client.login(username="learner", password=self.password)

        response = self.client.post(reverse("skill_request_application_accept", args=[application.pk]))

        booking = Booking.objects.get(learner=self.learner, tutor=self.tutor)
        self.assertRedirects(response, reverse("booking_detail", args=[booking.pk]))
        application.refresh_from_db()
        skill_request.refresh_from_db()
        self.assertEqual(application.status, SkillRequestApplication.STATUS_ACCEPTED)
        self.assertEqual(skill_request.status, SkillRequest.STATUS_FULFILLED)
        self.assertEqual(booking.status, Booking.STATUS_ACCEPTED)
        self.assertFalse(booking.listing.is_public)

        listing_response = self.client.get(reverse("listing_list"))
        self.assertNotContains(listing_response, booking.listing.title)

        detail_response = self.client.get(reverse("listing_detail", args=[booking.listing.pk]))
        self.assertEqual(detail_response.status_code, 404)

    def test_tutor_cannot_apply_to_own_skill_request(self):
        skill_request = SkillRequest.objects.create(
            learner=self.tutor,
            title="Need design help",
            category="design",
            description="Portfolio review.",
            availability="Friday",
        )
        self.client.login(username="tutor", password=self.password)

        response = self.client.post(
            reverse("skill_request_apply", args=[skill_request.pk]),
            {"pitch": "Applying to myself."},
        )

        self.assertRedirects(response, reverse("skill_request_detail", args=[skill_request.pk]))
        self.assertFalse(SkillRequestApplication.objects.exists())

    def _create_booking(self, status):
        return Booking.objects.create(
            listing=self.listing,
            learner=self.learner,
            tutor=self.tutor,
            requested_time=timezone.now() + timedelta(days=1),
            message="Can we schedule a session?",
            status=status,
        )
