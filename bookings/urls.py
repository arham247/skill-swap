from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("listings/<int:pk>/book/", views.booking_create_view, name="booking_create"),
    path("bookings/<int:pk>/", views.booking_detail_view, name="booking_detail"),
    path("bookings/<int:pk>/accept/", views.booking_accept_view, name="booking_accept"),
    path("bookings/<int:pk>/reject/", views.booking_reject_view, name="booking_reject"),
    path("bookings/<int:pk>/complete/", views.booking_complete_view, name="booking_complete"),
    path("bookings/<int:pk>/cancel/", views.booking_cancel_view, name="booking_cancel"),
    path("bookings/<int:pk>/review/", views.review_create_view, name="review_create"),
    path("requests/", views.skill_request_list_view, name="skill_request_list"),
    path("requests/create/", views.skill_request_create_view, name="skill_request_create"),
    path("requests/<int:pk>/", views.skill_request_detail_view, name="skill_request_detail"),
    path("requests/<int:pk>/apply/", views.skill_request_apply_view, name="skill_request_apply"),
    path(
        "applications/<int:pk>/accept/",
        views.skill_request_application_accept_view,
        name="skill_request_application_accept",
    ),
]
