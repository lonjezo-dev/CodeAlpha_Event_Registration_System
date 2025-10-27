from django.shortcuts import render
from .models import Event
from django.views import generic

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
        return render(request, 'events/event_detail.html', {'error_message': 'Event not found.'})
    return render(request, 'events/event_detail.html', {'event': event})

def create_event(request): 
    if request.method == 'POST':
        event_title = request.POST.get('title')
        if event_title:
            Event.objects.create(name=event_title)
            return render(request, 'events/create_event.html', {'success_message': 'Event created successfully!'})
        else:
            return render(request, 'events/create_event.html', {'error_message': 'Event name cannot be empty.'})
    return render(request, 'events/create_event.html')