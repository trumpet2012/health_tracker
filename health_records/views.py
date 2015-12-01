from django.views.generic import ListView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from django.db.models import Q

from .models import HealthProfile, HealthRecord, PhysActivity, EatingInfo
from .forms import PhysicalForm, RecordForm, BreakfastForm, LunchForm, DinnerForm


class ProfileListing(ListView):
    model = HealthProfile
    template_name = 'health_records/profile_listing.html'
    paginate_by = 10


def profile_page(request, profile_id):
    template = 'health_records/user_profile.html'
    context = {}
    try:
        profile = HealthProfile.objects.get(user_id=profile_id)
        records = profile.records.order_by('-activity_date')
        if records:
            latest_record = records[0]
            context.update({
                'latest_record': latest_record,
            })

        context.update({
            'profile': profile,
            'is_user': request.user == profile.user
        })

    except ObjectDoesNotExist:
        return HttpResponse("<h1>No profile with id: %s was found!</h1>" % profile_id)

    return render_to_response(template, context)


def create_profile(request, profile_id):
    profile = HealthProfile.objects.get(pk=profile_id)

    template = 'health_records/create_health_record.html'
    context = {
        'profile': profile,
    }
    context.update(csrf(request))

    if request.method == 'GET':
        context.update({
            'record_form': RecordForm(),
            'phys_form': PhysicalForm(),
            'breakfast_form': BreakfastForm(),
            'lunch_form': LunchForm(),
            'dinner_form': DinnerForm(),
        })

    if request.method == 'POST':
        form_data = request.POST

        record_form = RecordForm(form_data)
        phys_form = PhysicalForm(form_data)
        breakfast_form = BreakfastForm(form_data)
        lunch_form = LunchForm(form_data)
        dinner_form = DinnerForm(form_data)

        phys_error = False
        eat_errors = False

        if record_form.is_valid():
            record_data = record_form.cleaned_data
            record = HealthRecord.objects.create(profile=profile, **record_data)
            record.save()

            if phys_form.is_valid():
                phys_data = phys_form.cleaned_data
                physical_info = PhysActivity.objects.create(record=record, **phys_data)
                physical_info.save()
            elif phys_form.data['activity_type']:
                phys_error = True

            if breakfast_form.changed_data:
                if breakfast_form.is_valid():
                    breakfast_data = breakfast_form.cleaned_data
                    breakfast_info = EatingInfo.objects.create(record=record, meal_time=breakfast_form.meal_time, calories=breakfast_data.get('breakfast_calories'))
                    breakfast_info.save()
                else:
                    eat_errors = True

            if lunch_form.changed_data:
                if lunch_form.is_valid():
                    lunch_data = lunch_form.cleaned_data
                    lunch_info = EatingInfo.objects.create(record=record, meal_time=lunch_form.meal_time, calories=lunch_data.get('lunch_calories'))
                    lunch_info.save()
                else:
                    eat_errors = True

            if  dinner_form.changed_data:
                if dinner_form.is_valid():
                    dinner_data = dinner_form.cleaned_data
                    dinner_info = EatingInfo.objects.create(record=record, meal_time=dinner_form.meal_time, calories=dinner_data.get('dinner_calories'))
                    dinner_info.save()
                else:
                    eat_errors = True

        if record_form.errors or phys_error or eat_errors:
            context.update({
                'record_form': record_form,
                'phys_form': phys_form,
                'breakfast_form': breakfast_form,
                'lunch_form': lunch_form,
                'dinner_form': dinner_form,
            })
        else:
            return HttpResponseRedirect(reverse('profile_page', args=(profile_id,))+"?msg=Health%20records%20updated.")

    return render_to_response(template, context=context)


def profile(request):
    if request.user.is_authenticated():
        health_profile = HealthProfile.objects.get(user=request.user)
        return HttpResponseRedirect(reverse('profile_page', args=(health_profile.user_id,)))
    else:
        return HttpResponseRedirect(reverse('admin:login')+"?next="+reverse('profile'), )


def profile_records_json(request, profile_id):
    try:
        profile = HealthProfile.objects.get(pk=profile_id)
    except HealthProfile.DoesNotExist:
        return JsonResponse({"error": "Profile with specified id does not exist."})


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
