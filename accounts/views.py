from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from .forms import (
    OTPPasswordResetConfirmForm,
    OTPPasswordResetRequestForm,
    ProfileUpdateForm,
    RegistrationForm,
    SkillSwapAuthenticationForm,
)
from .models import User


class SkillSwapLoginView(LoginView):
    authentication_form = SkillSwapAuthenticationForm
    template_name = "accounts/login.html"


class SkillSwapLogoutView(LogoutView):
    pass


def register_view(request):
    if request.user.is_authenticated:
        return redirect("listing_list")

    form = RegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Your account has been created.")
        return redirect("listing_list")

    return render(request, "accounts/register.html", {"form": form})


@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")


@login_required
def profile_edit_view(request):
    form = ProfileUpdateForm(request.POST or None, instance=request.user)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Profile updated successfully.")
        return redirect("profile")

    return render(request, "accounts/profile_edit.html", {"form": form})


def password_reset_request_view(request):
    form = OTPPasswordResetRequestForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = User.objects.get(email=form.cleaned_data["email"])
        otp = user.create_reset_otp()
        messages.info(
            request,
            f"Reset OTP generated. For development, use this code: {otp}",
        )
        return redirect("password_reset_verify")

    return render(request, "accounts/password_reset_request.html", {"form": form})


def password_reset_verify_view(request):
    form = OTPPasswordResetConfirmForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.user
        user.set_password(form.cleaned_data["new_password1"])
        user.clear_reset_otp()
        user.save()
        messages.success(request, "Password reset successfully. Please log in.")
        return redirect("login")

    return render(request, "accounts/password_reset_verify.html", {"form": form})
