from django.urls import path

from .views import (
    ListingCreateView,
    ListingDeleteView,
    ListingDetailView,
    ListingListView,
    ListingUpdateView,
)

urlpatterns = [
    path("", ListingListView.as_view(), name="listing_list"),
    path("listings/create/", ListingCreateView.as_view(), name="listing_create"),
    path("listings/<int:pk>/", ListingDetailView.as_view(), name="listing_detail"),
    path("listings/<int:pk>/edit/", ListingUpdateView.as_view(), name="listing_edit"),
    path("listings/<int:pk>/delete/", ListingDeleteView.as_view(), name="listing_delete"),
]
