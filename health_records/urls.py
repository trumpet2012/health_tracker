from django.conf.urls import url

from .views import ProfileListing

from health_records import views

urlpatterns = [
    url('^all/$', ProfileListing.as_view(), name='profile_listing'),
    url('^profile/$', views.profile_page, name='profile_page'),
]
