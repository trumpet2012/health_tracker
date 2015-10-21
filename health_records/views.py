from django.views.generic import ListView

from .models import HealthProfile


class ProfileListing(ListView):
    model = HealthProfile
    template_name = 'health_records/profile_listing.html'

