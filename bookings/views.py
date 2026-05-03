from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from listings.models import Listing

from .forms import (
    BookingMessageForm,
    BookingRequestForm,
    ReviewForm,
    SkillRequestApplicationForm,
    SkillRequestForm,
)
from .models import Booking, Review, SkillRequest, SkillRequestApplication


@login_required
def dashboard_view(request):
    learner_bookings = Booking.objects.filter(learner=request.user).select_related("listing", "tutor")
    tutor_bookings = Booking.objects.filter(tutor=request.user).select_related("listing", "learner")
    skill_requests = SkillRequest.objects.filter(learner=request.user)
    applications = SkillRequestApplication.objects.filter(tutor=request.user).select_related("skill_request")
    return render(
        request,
        "bookings/dashboard.html",
        {
            "learner_bookings": learner_bookings,
            "tutor_bookings": tutor_bookings,
            "skill_requests": skill_requests,
            "applications": applications,
        },
    )


@login_required
def booking_create_view(request, pk):
    listing = get_object_or_404(Listing, pk=pk, is_public=True)
    if listing.tutor == request.user:
        messages.warning(request, "You cannot book your own listing.")
        return redirect(listing)
    existing_booking = Booking.objects.filter(
        listing=listing,
        learner=request.user,
        status__in=Booking.ACTIVE_STATUSES,
    ).first()
    if existing_booking:
        messages.warning(request, "You already have an active booking for this listing.")
        return redirect(existing_booking)

    form = BookingRequestForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        booking = form.save(commit=False)
        booking.listing = listing
        booking.learner = request.user
        booking.tutor = listing.tutor
        booking.save()
        messages.success(request, "Booking request sent to the tutor.")
        return redirect(booking)

    return render(request, "bookings/booking_form.html", {"form": form, "listing": listing})


@login_required
def booking_detail_view(request, pk):
    booking = get_object_or_404(
        Booking.objects.select_related("listing", "learner", "tutor"),
        pk=pk,
    )
    if request.user not in {booking.learner, booking.tutor}:
        return render(request, "403.html", status=403)

    message_form = BookingMessageForm(request.POST or None)
    if request.method == "POST":
        if not booking.can_message:
            messages.warning(request, "Messages open after the booking is accepted.")
            return redirect(booking)
        if message_form.is_valid():
            booking_message = message_form.save(commit=False)
            booking_message.booking = booking
            booking_message.sender = request.user
            booking_message.save()
            return redirect(booking)

    return render(
        request,
        "bookings/booking_detail.html",
        {
            "booking": booking,
            "message_form": message_form,
            "messages_for_booking": booking.messages.select_related("sender"),
            "can_review": _can_review(request.user, booking),
        },
    )


@login_required
@require_POST
def booking_accept_view(request, pk):
    booking = get_object_or_404(Booking, pk=pk, tutor=request.user)
    if booking.status == Booking.STATUS_PENDING:
        booking.status = Booking.STATUS_ACCEPTED
        booking.save(update_fields=["status", "updated_at"])
        messages.success(request, "Booking accepted.")
    return redirect(booking)


@login_required
@require_POST
def booking_reject_view(request, pk):
    booking = get_object_or_404(Booking, pk=pk, tutor=request.user)
    if booking.status == Booking.STATUS_PENDING:
        booking.status = Booking.STATUS_REJECTED
        booking.save(update_fields=["status", "updated_at"])
        messages.success(request, "Booking rejected.")
    return redirect(booking)


@login_required
@require_POST
def booking_complete_view(request, pk):
    booking = get_object_or_404(Booking, pk=pk, tutor=request.user)
    if booking.status == Booking.STATUS_ACCEPTED:
        booking.status = Booking.STATUS_COMPLETED
        booking.save(update_fields=["status", "updated_at"])
        messages.success(request, "Booking marked as completed.")
    return redirect(booking)


@login_required
@require_POST
def booking_cancel_view(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.user not in {booking.learner, booking.tutor}:
        return render(request, "403.html", status=403)
    if booking.status in {Booking.STATUS_PENDING, Booking.STATUS_ACCEPTED}:
        booking.status = Booking.STATUS_CANCELLED
        booking.save(update_fields=["status", "updated_at"])
        messages.success(request, "Booking cancelled.")
    return redirect(booking)


@login_required
def review_create_view(request, pk):
    booking = get_object_or_404(Booking.objects.select_related("tutor", "learner"), pk=pk)
    if not _can_review(request.user, booking):
        messages.warning(request, "This booking is not ready for review.")
        return redirect(booking)

    form = ReviewForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        review = form.save(commit=False)
        review.booking = booking
        review.reviewer = request.user
        review.tutor = booking.tutor
        review.save()
        messages.success(request, "Review submitted.")
        return redirect(booking)

    return render(request, "bookings/review_form.html", {"form": form, "booking": booking})


def skill_request_list_view(request):
    skill_requests = SkillRequest.objects.select_related("learner").filter(status=SkillRequest.STATUS_OPEN)
    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    if query:
        skill_requests = skill_requests.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(learner__username__icontains=query)
        )
    if category:
        skill_requests = skill_requests.filter(category=category)
    return render(
        request,
        "skill_requests/skill_request_list.html",
        {"skill_requests": skill_requests, "categories": Listing.CATEGORY_CHOICES},
    )


@login_required
def skill_request_create_view(request):
    form = SkillRequestForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        skill_request = form.save(commit=False)
        skill_request.learner = request.user
        skill_request.save()
        messages.success(request, "Skill request posted.")
        return redirect(skill_request)
    return render(request, "skill_requests/skill_request_form.html", {"form": form})


def skill_request_detail_view(request, pk):
    skill_request = get_object_or_404(
        SkillRequest.objects.select_related("learner").prefetch_related("applications__tutor"),
        pk=pk,
    )
    return render(
        request,
        "skill_requests/skill_request_detail.html",
        {"skill_request": skill_request},
    )


@login_required
def skill_request_apply_view(request, pk):
    skill_request = get_object_or_404(SkillRequest, pk=pk, status=SkillRequest.STATUS_OPEN)
    if skill_request.learner == request.user:
        messages.warning(request, "You cannot apply to your own request.")
        return redirect(skill_request)
    if SkillRequestApplication.objects.filter(skill_request=skill_request, tutor=request.user).exists():
        messages.warning(request, "You have already applied to this request.")
        return redirect(skill_request)

    form = SkillRequestApplicationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        application = form.save(commit=False)
        application.skill_request = skill_request
        application.tutor = request.user
        application.save()
        messages.success(request, "Application submitted.")
        return redirect(skill_request)
    return render(
        request,
        "skill_requests/application_form.html",
        {"form": form, "skill_request": skill_request},
    )


@login_required
@require_POST
def skill_request_application_accept_view(request, pk):
    application = get_object_or_404(
        SkillRequestApplication.objects.select_related("skill_request", "tutor"),
        pk=pk,
        skill_request__learner=request.user,
        status=SkillRequestApplication.STATUS_PENDING,
    )
    skill_request = application.skill_request

    listing = Listing.objects.create(
        tutor=application.tutor,
        title=skill_request.title,
        category=skill_request.category,
        description=skill_request.description,
        availability=skill_request.availability,
        is_public=False,
    )
    booking = Booking.objects.create(
        listing=listing,
        learner=request.user,
        tutor=application.tutor,
        requested_time=skill_request.created_at,
        message=application.pitch,
        status=Booking.STATUS_ACCEPTED,
    )
    application.status = SkillRequestApplication.STATUS_ACCEPTED
    application.booking = booking
    application.save(update_fields=["status", "booking"])
    skill_request.applications.exclude(pk=application.pk).update(
        status=SkillRequestApplication.STATUS_REJECTED
    )
    skill_request.status = SkillRequest.STATUS_FULFILLED
    skill_request.save(update_fields=["status", "updated_at"])
    messages.success(request, "Application accepted and booking created.")
    return redirect(booking)


def _can_review(user, booking):
    return (
        user == booking.learner
        and booking.status == Booking.STATUS_COMPLETED
        and not hasattr(booking, "review")
    )
