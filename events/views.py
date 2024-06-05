from django.shortcuts import render
from django.views import generic
from .models import Events

# Create your views here.
def about_events(request):

    events = events = Events.objects.all().first()

    return render(
        request,
        "events/events.html",
        {
            "events": events,
        }
    )