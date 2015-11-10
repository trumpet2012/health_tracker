from django.views.generic import ListView

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import HealthProfile


class ProfileListing(ListView):
    model = HealthProfile
    template_name = 'health_records/profile_listing.html'


def profile_page(request):
    template = 'health_records/user_profile.html'
    username = request.user
    try:
        profile = HealthProfile.objects.get(user__username=username)
    except ObjectDoesNotExist:
        return HttpResponse("<h1>Must be logged in to view your profile (this should change later)</h1>")

    context = {
        'profile': profile
    }

    return render_to_response(template, context)
