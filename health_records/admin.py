from django.contrib import admin

from . import models

admin.site.register(models.HealthProfile)
admin.site.register(models.HealthRecord)
admin.site.register(models.PhysActivity)
admin.site.register(models.EatingInfo)
