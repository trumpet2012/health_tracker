from django.views.generic import ListView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from .models import HealthProfile
from .forms import EatingForm, PhysicalForm, RecordForm


class ProfileListing(ListView):
    model = HealthProfile
    template_name = 'health_records/profile_listing.html'
    paginate_by = 10


def profile_page(request, profile_id):
    template = 'health_records/user_profile.html'
    try:
        profile = HealthProfile.objects.get(user_id=profile_id)
    except ObjectDoesNotExist:
        return HttpResponse("<h1>No profile with id: %s was found!</h1>" % profile_id)

    context = {
        'profile': profile
    }

    return render_to_response(template, context)


def create_profile(request, profile_id):
    profile = HealthProfile.objects.get(pk=profile_id)

    template = 'health_records/create_health_record.html'
    context = {
        'profile': profile,
    }

    if request.method == 'GET':
        context.update({
            'record_form': RecordForm(),
            'phys_form': PhysicalForm(),
            'eat_form': EatingForm(),
        })

    if request.method == 'POST':
        pass

    return render_to_response(template, context=context)



def profile(request):
    if request.user.is_authenticated():
        health_profile = HealthProfile.objects.get(user=request.user)
        return HttpResponseRedirect(reverse('profile_page', args=(health_profile.user_id,)))
    else:
        return HttpResponseRedirect(reverse('admin:index'), )


def search(request, search_string):
    template = "health_records/profile_listing.html"
    object_list = HealthProfile.objects.filter(
        Q(user__username__contains=search_string) |
        Q(user__first_name__contains=search_string) |
        Q(user__last_name__contains=search_string) |
        Q(user__email__contains=search_string)
    )

    context = {
        'object_list': object_list
    }

    return render_to_response(template, context)
