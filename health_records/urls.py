from django.conf.urls import url

from .views import ProfileListing

from health_records import views

urlpatterns = [
    url('^all/$', ProfileListing.as_view(), name='profile_listing'),
    url('^profile/(?P<profile_id>\d+)/$', views.profile_page, name='profile_page'),
    url('^profile/', views.profile, name='profile'),
    url('^search/(?P<search_string>.*)$', views.search, name='search'),
    url('^create-record/(?P<profile_id>\d+)/$', views.create_profile, name='create_record')
]
