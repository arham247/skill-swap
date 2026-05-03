from django import forms

from .models import Booking, BookingMessage, Review, SkillRequest, SkillRequestApplication


class BookingRequestForm(forms.ModelForm):
    requested_time = forms.DateTimeField(
        input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M:%S"],
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
    )

    class Meta:
        model = Booking
        fields = ("requested_time", "message")
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),
        }


class BookingMessageForm(forms.ModelForm):
    class Meta:
        model = BookingMessage
        fields = ("body",)
        widgets = {"body": forms.Textarea(attrs={"rows": 3, "placeholder": "Write a message..."})}


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("rating", "comment")
        widgets = {
            "rating": forms.NumberInput(attrs={"min": 1, "max": 5}),
            "comment": forms.Textarea(attrs={"rows": 4}),
        }


class SkillRequestForm(forms.ModelForm):
    class Meta:
        model = SkillRequest
        fields = ("title", "category", "description", "availability")
        widgets = {"description": forms.Textarea(attrs={"rows": 5})}


class SkillRequestApplicationForm(forms.ModelForm):
    class Meta:
        model = SkillRequestApplication
        fields = ("pitch",)
        widgets = {"pitch": forms.Textarea(attrs={"rows": 4})}
