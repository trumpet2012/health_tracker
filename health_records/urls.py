from django.conf.urls import url

from .views import ProfileListing

urlpatterns = [
    url('^all/$', ProfileListing.as_view(), name='profile_listing')
]
