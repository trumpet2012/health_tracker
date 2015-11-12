import math

from django.db import models
from django.contrib.auth.models import User

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey


class HealthProfile(ClusterableModel):
    class Meta:
        verbose_name = 'Health Profile'

    user = models.OneToOneField(User, primary_key=True)
    height = models.FloatField(help_text="Height in inches")
    weight = models.FloatField(help_text="Weight in pounds")

    def __str__(self):
        return self.user.username

    def height_in_feet_and_inches(self):
        """
        Helper method that will convert the height in inches into feet and inches.
        :return: A tuple of the form (feet, inches)
        """
        height = self.height
        height_feet = height / 12
        inches, feet = math.modf(height_feet)
        feet = int(feet)
        inches *= 12
        inches = round(inches, 2)
        inches_frac, inches_whole = math.modf(inches)
        if not inches_frac:
            inches = int(inches)

        return feet, inches

    def calculate_bmi(self):
        return (self.weight/(self.height*self.height))*703

class HealthRecord(ClusterableModel):
    profile = ParentalKey(HealthProfile, related_name='records')
    activity_date = models.DateField()
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    weight = models.FloatField(help_text="Enter your weight in lbs.")

    def __str__(self):
        return self.profile.user.username + ':' + self.activity_date.strftime('%b %d, %Y')


class PhysActivity(ClusterableModel):
    PUSHUPS = 'pushups'
    SITUPS = 'situps'
    CRUNCHES = 'crunches'
    PULLUPS = 'pullups'
    BENCH_PRESSES = 'bench_presses'
    JOGGING = 'jogging'
    WALKING = 'walking'
    BIKING = 'biking'
    ACTIVITY_CHOICES = (
        (PUSHUPS, 'Pushups'),
        (SITUPS, 'Situps'),
        (CRUNCHES, 'Crunches'),
        (PULLUPS, 'Pullups'),
        (BENCH_PRESSES, 'Bench Presses'),
        (JOGGING, 'Jogging'),
        (WALKING, 'Walking'),
        (BIKING, 'Biking'),
    )
    record = ParentalKey(HealthRecord, related_name='physical_activity')
    activity_type = models.CharField(choices=ACTIVITY_CHOICES, max_length=255)
    duration = models.IntegerField(help_text='The duration of the activity in minutes.')
    reps = models.IntegerField(help_text='Number of times you performed the exercise.')

    def __str__(self):
        return self.record.profile.user.username + '-' + \
               self.record.activity_date.strftime('%b %d, %Y') \
               + ':' + self.activity_type


class EatingInfo(ClusterableModel):
    BREAKFAST = 'breakfast'
    LUNCH = 'lunch'
    DINNER = 'dinner'
    MEAL_CHOICES = (
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
    )
    record = ParentalKey(HealthRecord, related_name='eating_info')
    meal_time = models.CharField(choices=MEAL_CHOICES, max_length=255)
    calories = models.IntegerField(help_text='The number of calories of the meal.')

    def __str__(self):
        return self.record.profile.user.username + '-' + \
               self.record.activity_date.strftime('%b %d, %Y') \
               + ':' + self.meal_time
