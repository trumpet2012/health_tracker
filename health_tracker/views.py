from django.views.generic.base import TemplateView
from django.http import HttpResponse


class IndexView(TemplateView):
    template_name = 'index.html'


def login(request):
    return HttpResponse("<h1>Must be logged in to view your profile (this should change later)</h1>")
