from django import forms

from .models import HealthRecord, PhysActivity, EatingInfo


class RecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['activity_date', 'weight', ]


class PhysicalForm(forms.ModelForm):
    class Meta:
        model = PhysActivity
        exclude = ['record', ]


class EatingForm(forms.ModelForm):
    class Meta:
        model = EatingInfo
        exclude = ['record', ]


class BreakfastForm(forms.Form):
    meal_time = 'breakfast'
    breakfast_calories = forms.IntegerField()


class LunchForm(forms.Form):
    meal_time = 'lunch'
    lunch_calories = forms.IntegerField()


class DinnerForm(forms.Form):
    meal_time = 'dinner'
    dinner_calories = forms.IntegerField()
