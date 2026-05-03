from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from bookings.models import Booking

from .forms import ListingForm
from .models import Listing


class ListingListView(ListView):
    model = Listing
    template_name = "listings/listing_list.html"
    context_object_name = "listings"
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_public=True)
        query = self.request.GET.get("q", "").strip()
        category = self.request.GET.get("category", "").strip()

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(tutor__username__icontains=query)
            )
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Listing.CATEGORY_CHOICES
        return context


class ListingDetailView(DetailView):
    model = Listing
    template_name = "listings/listing_detail.html"
    context_object_name = "listing"

    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated and user != self.object.tutor:
            context["existing_booking"] = self.object.bookings.filter(
                learner=user,
                status__in=Booking.ACTIVE_STATUSES,
            ).first()
        return context


class OwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().tutor == self.request.user


class ListingCreateView(LoginRequiredMixin, CreateView):
    model = Listing
    form_class = ListingForm
    template_name = "listings/listing_form.html"

    def form_valid(self, form):
        form.instance.tutor = self.request.user
        messages.success(self.request, "Listing created successfully.")
        return super().form_valid(form)


class ListingUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Listing
    form_class = ListingForm
    template_name = "listings/listing_form.html"

    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)

    def form_valid(self, form):
        messages.success(self.request, "Listing updated successfully.")
        return super().form_valid(form)


class ListingDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Listing
    template_name = "listings/listing_confirm_delete.html"
    success_url = "/"

    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)

    def form_valid(self, form):
        messages.success(self.request, "Listing deleted successfully.")
        return super().form_valid(form)
