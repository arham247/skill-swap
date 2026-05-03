from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

User = get_user_model()


class AuthenticationFlowTests(TestCase):
    def setUp(self):
        self.password = "StrongPass123!"
        self.user = User.objects.create_user(
            username="user1",
            email="user1@example.com",
            password=self.password,
            first_name="Faraz",
        )

    def test_user_can_register(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "faraz",
                "email": "faraz@example.com",
                "first_name": "Faraz",
                "last_name": "Ali",
                "bio": "Backend student",
                "listed_skills": "Python, SQL",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
        )

        self.assertRedirects(response, reverse("listing_list"))
        self.assertTrue(User.objects.filter(username="faraz").exists())

    def test_registration_rejects_duplicate_username(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": self.user.username,
                "email": "new@example.com",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "already exists")

    def test_registration_rejects_duplicate_email(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "newuser",
                "email": self.user.email,
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "already exists")

    def test_registration_rejects_mismatched_passwords(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "newuser",
                "email": "new@example.com",
                "password1": "StrongPass123!",
                "password2": "WrongPass123!",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("password2", response.context["form"].errors)

    def test_registration_rejects_weak_password(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "weakuser",
                "email": "weak@example.com",
                "password1": "12345678",
                "password2": "12345678",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["form"].errors)

    def test_login_with_valid_credentials(self):
        response = self.client.post(
            reverse("login"),
            {"username": self.user.username, "password": self.password},
        )

        self.assertRedirects(response, reverse("listing_list"))

    def test_login_rejects_invalid_password(self):
        response = self.client.post(
            reverse("login"),
            {"username": self.user.username, "password": "WrongPass123!"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a correct username and password")

    def test_logout_clears_authenticated_session(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.post(reverse("logout"))

        self.assertRedirects(response, reverse("login"))
        profile_response = self.client.get(reverse("profile"))
        self.assertRedirects(profile_response, f"{reverse('login')}?next={reverse('profile')}")

    def test_profile_page_requires_login(self):
        response = self.client.get(reverse("profile"))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('profile')}")

    def test_logged_in_user_can_view_profile_page(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(reverse("profile"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.email)

    def test_profile_edit_updates_user_details(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.post(
            reverse("profile_edit"),
            {
                "first_name": "Updated",
                "last_name": "User",
                "email": "updated@example.com",
                "bio": "Updated bio",
                "listed_skills": "Python, Django",
            },
        )

        self.assertRedirects(response, reverse("profile"))
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "Updated")
        self.assertEqual(self.user.email, "updated@example.com")

    def test_profile_edit_rejects_duplicate_email(self):
        other_user = User.objects.create_user(
            username="user2",
            email="user2@example.com",
            password="StrongPass123!",
        )
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.post(
            reverse("profile_edit"),
            {
                "first_name": self.user.first_name,
                "last_name": self.user.last_name,
                "email": other_user.email,
                "bio": self.user.bio,
                "listed_skills": self.user.listed_skills,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["form"].errors)

    def test_password_reset_request_generates_otp(self):
        response = self.client.post(
            reverse("password_reset_request"),
            {"email": self.user.email},
            follow=True,
        )

        self.user.refresh_from_db()
        self.assertRedirects(response, reverse("password_reset_verify"))
        self.assertEqual(len(self.user.reset_otp), 6)

    def test_password_reset_request_rejects_unknown_email(self):
        response = self.client.post(
            reverse("password_reset_request"),
            {"email": "missing@example.com"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No account was found")

    def test_password_reset_with_otp(self):
        otp = self.user.create_reset_otp()

        response = self.client.post(
            reverse("password_reset_verify"),
            {
                "email": self.user.email,
                "otp": otp,
                "new_password1": "NewPass123!",
                "new_password2": "NewPass123!",
            },
        )

        self.assertRedirects(response, reverse("login"))
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("NewPass123!"))

    def test_password_reset_rejects_invalid_otp(self):
        self.user.create_reset_otp()
        response = self.client.post(
            reverse("password_reset_verify"),
            {
                "email": self.user.email,
                "otp": "000000",
                "new_password1": "NewPass123!",
                "new_password2": "NewPass123!",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "OTP is invalid or has expired")

    def test_password_reset_rejects_expired_otp(self):
        self.user.reset_otp = "123456"
        self.user.reset_otp_expires_at = timezone.now() - timedelta(minutes=1)
        self.user.save(update_fields=["reset_otp", "reset_otp_expires_at"])

        response = self.client.post(
            reverse("password_reset_verify"),
            {
                "email": self.user.email,
                "otp": "123456",
                "new_password1": "NewPass123!",
                "new_password2": "NewPass123!",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "OTP is invalid or has expired")

    def test_password_reset_rejects_mismatched_new_passwords(self):
        otp = self.user.create_reset_otp()
        response = self.client.post(
            reverse("password_reset_verify"),
            {
                "email": self.user.email,
                "otp": otp,
                "new_password1": "NewPass123!",
                "new_password2": "DifferentPass123!",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "do not match")

    def test_password_reset_rejects_weak_new_password(self):
        otp = self.user.create_reset_otp()
        response = self.client.post(
            reverse("password_reset_verify"),
            {
                "email": self.user.email,
                "otp": otp,
                "new_password1": "12345678",
                "new_password2": "12345678",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["form"].errors)
