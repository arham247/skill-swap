from django.test import TestCase
from django.urls import reverse

from accounts.models import User

from .models import Listing


class ListingTests(TestCase):
    def setUp(self):
        self.password = "StrongPass123!"
        self.user = User.objects.create_user(
            username="mentor",
            email="mentor@example.com",
            password=self.password,
        )
        self.other_user = User.objects.create_user(
            username="other",
            email="other@example.com",
            password=self.password,
        )
        self.listing = Listing.objects.create(
            tutor=self.user,
            title="Python Fundamentals",
            category="programming",
            description="Learn loops, functions, and debugging.",
            availability="Weekdays after 6 PM",
        )

    def test_listing_page_loads(self):
        response = self.client.get(reverse("listing_list"))
        self.assertEqual(response.status_code, 200)

    def test_listing_page_shows_existing_listing(self):
        response = self.client.get(reverse("listing_list"))
        self.assertContains(response, self.listing.title)

    def test_listing_detail_page_loads(self):
        response = self.client.get(reverse("listing_detail", args=[self.listing.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.listing.description)

    def test_listing_detail_page_returns_404_for_missing_listing(self):
        response = self.client.get(reverse("listing_detail", args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_authenticated_user_can_create_listing(self):
        self.client.login(username="mentor", password=self.password)
        response = self.client.post(
            reverse("listing_create"),
            {
                "title": "Django Basics",
                "category": "programming",
                "description": "Build your first Django app.",
                "availability": "Weekends",
            },
        )

        listing = Listing.objects.get(title="Django Basics")
        self.assertRedirects(response, reverse("listing_detail", args=[listing.pk]))
        self.assertEqual(listing.tutor, self.user)

    def test_listing_create_requires_login(self):
        response = self.client.get(reverse("listing_create"))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('listing_create')}")

    def test_listing_create_rejects_blank_required_fields(self):
        self.client.login(username="mentor", password=self.password)
        response = self.client.post(
            reverse("listing_create"),
            {
                "title": "",
                "category": "",
                "description": "",
                "availability": "",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["form"].errors)

    def test_listing_create_rejects_invalid_category(self):
        self.client.login(username="mentor", password=self.password)
        response = self.client.post(
            reverse("listing_create"),
            {
                "title": "Invalid Category Listing",
                "category": "invalid",
                "description": "Description",
                "availability": "Anytime",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["form"].errors)

    def test_owner_can_update_listing(self):
        self.client.login(username="mentor", password=self.password)
        response = self.client.post(
            reverse("listing_edit", args=[self.listing.pk]),
            {
                "title": "Advanced Python Fundamentals",
                "category": "programming",
                "description": "Updated description",
                "availability": "Fridays",
            },
        )

        self.assertRedirects(response, reverse("listing_detail", args=[self.listing.pk]))
        self.listing.refresh_from_db()
        self.assertEqual(self.listing.title, "Advanced Python Fundamentals")

    def test_non_owner_cannot_update_listing(self):
        self.client.login(username="other", password=self.password)
        response = self.client.post(
            reverse("listing_edit", args=[self.listing.pk]),
            {
                "title": "Hacked Title",
                "category": "programming",
                "description": "Hacked description",
                "availability": "Always",
            },
        )

        self.assertEqual(response.status_code, 403)
        self.listing.refresh_from_db()
        self.assertNotEqual(self.listing.title, "Hacked Title")

    def test_owner_can_delete_listing(self):
        self.client.login(username="mentor", password=self.password)
        response = self.client.post(reverse("listing_delete", args=[self.listing.pk]))

        self.assertRedirects(response, reverse("listing_list"))
        self.assertFalse(Listing.objects.filter(pk=self.listing.pk).exists())

    def test_non_owner_cannot_delete_listing(self):
        self.client.login(username="other", password=self.password)
        response = self.client.post(reverse("listing_delete", args=[self.listing.pk]))

        self.assertEqual(response.status_code, 403)
        self.assertTrue(Listing.objects.filter(pk=self.listing.pk).exists())

    def test_listing_edit_requires_login(self):
        response = self.client.get(reverse("listing_edit", args=[self.listing.pk]))
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('listing_edit', args=[self.listing.pk])}",
        )

    def test_listing_delete_requires_login(self):
        response = self.client.get(reverse("listing_delete", args=[self.listing.pk]))
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('listing_delete', args=[self.listing.pk])}",
        )

    def test_listing_search_filters_by_title(self):
        response = self.client.get(reverse("listing_list"), {"q": "Python"})
        self.assertContains(response, self.listing.title)

    def test_listing_search_returns_no_match_when_query_missing(self):
        response = self.client.get(reverse("listing_list"), {"q": "Nonexistent"})
        self.assertNotContains(response, self.listing.title)
        self.assertContains(response, "No listings found")

    def test_listing_filter_by_category(self):
        Listing.objects.create(
            tutor=self.user,
            title="Graphic Design",
            category="design",
            description="Design basics",
            availability="Mondays",
        )

        response = self.client.get(reverse("listing_list"), {"category": "design"})
        self.assertContains(response, "Graphic Design")
        self.assertNotContains(response, self.listing.title)

    def test_listing_combined_search_and_category_filter(self):
        Listing.objects.create(
            tutor=self.user,
            title="Python for Data Analysis",
            category="programming",
            description="Pandas and NumPy",
            availability="Tuesdays",
        )
        Listing.objects.create(
            tutor=self.user,
            title="Business Writing",
            category="business",
            description="Professional communication",
            availability="Wednesdays",
        )

        response = self.client.get(
            reverse("listing_list"),
            {"q": "Python", "category": "programming"},
        )
        self.assertContains(response, "Python for Data Analysis")
        self.assertNotContains(response, "Business Writing")
