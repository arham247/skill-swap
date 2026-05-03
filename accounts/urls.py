from django.urls import path

from .views import (
    SkillSwapLoginView,
    SkillSwapLogoutView,
    password_reset_request_view,
    password_reset_verify_view,
    profile_edit_view,
    profile_view,
    register_view,
)

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", SkillSwapLoginView.as_view(), name="login"),
    path("logout/", SkillSwapLogoutView.as_view(), name="logout"),
    path("profile/", profile_view, name="profile"),
    path("profile/edit/", profile_edit_view, name="profile_edit"),
    path("forgot-password/", password_reset_request_view, name="password_reset_request"),
    path("verify-otp/", password_reset_verify_view, name="password_reset_verify"),
]
