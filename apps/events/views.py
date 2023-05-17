from django.shortcuts import render
from .models import Events

# Create your views here.

def events(request):
    events = Events.objects.all()

    context = {
        "events" : events
    }
    return render(request, "events.html", context)