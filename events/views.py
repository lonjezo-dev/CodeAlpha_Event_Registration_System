from django.shortcuts import render
from .models import Event

# Create your views here.
def index(request):
    events = Event.objects.all()
    # compute a boolean to avoid re-evaluating the queryset inside the template
    no_events = not events.exists()
    return render(request, 'events/index.html', {'events': events, 'no_events': no_events})

def detail(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        return render(request, 'events/detail.html', {'error_message': 'Event not found.'})
    return render(request, 'events/detail.html', {'event': event})