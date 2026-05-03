from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.password_validation import validate_password

from .models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "bio",
            "listed_skills",
            "password1",
            "password2",
        )


class SkillSwapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "bio", "listed_skills")


class OTPPasswordResetRequestForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No account was found with this email address.")
        return email


class OTPPasswordResetConfirmForm(forms.Form):
    email = forms.EmailField()
    otp = forms.CharField(max_length=6, min_length=6)
    new_password1 = forms.CharField(widget=forms.PasswordInput())
    new_password2 = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        otp = cleaned_data.get("otp")
        password1 = cleaned_data.get("new_password1")
        password2 = cleaned_data.get("new_password2")

        if not email or not otp:
            return cleaned_data

        try:
            self.user = User.objects.get(email=email)
        except User.DoesNotExist as exc:
            raise forms.ValidationError("Invalid email or OTP.") from exc

        if not self.user.otp_is_valid(otp):
            raise forms.ValidationError("OTP is invalid or has expired.")

        if password1 != password2:
            raise forms.ValidationError("The new passwords do not match.")

        validate_password(password1, self.user)

        return cleaned_data
