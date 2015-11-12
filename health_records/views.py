from django.views.generic import ListView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from health_tracker.views import login

from .models import HealthProfile


class ProfileListing(ListView):
    model = HealthProfile
    template_name = 'health_records/profile_listing.html'


def profile_page(request, profile_id):
    template = 'health_records/user_profile.html'
    try:
        profile = HealthProfile.objects.get(user_id=profile_id)
    except ObjectDoesNotExist:
        return HttpResponse("<h1>Must be logged in to view your profile (this should change later)</h1>")

    context = {
        'profile': profile
    }

    return render_to_response(template, context)

def profile(request):
    if request.user.is_authenticated():
        health_profile = HealthProfile.objects.get(user=request.user)
        return HttpResponseRedirect(reverse('profile_page', args=(health_profile.user_id,)))
    else:
        return HttpResponseRedirect(reverse('login'), )
