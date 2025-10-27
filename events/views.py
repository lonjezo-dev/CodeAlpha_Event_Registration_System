
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Registration
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


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


@login_required
@require_POST
def register_event(request, event_id):
    """Register the current authenticated user for the given event.

    - Creates a Registration if one doesn't exist.
    - Uses Django messages to report success or existing registration.
    - Redirects back to the event detail page.
    """
    event = get_object_or_404(Event, pk=event_id)

    created = Registration.objects.get_or_create(user=request.user, event=event)
    if created:
        messages.success(request, 'You have successfully registered for this event.')
    else:
        messages.info(request, 'You are already registered for this event.')

    # Redirect back to the event detail page using the app namespace
    try:
        return redirect('events:detail', event_id=event.id)
    except Exception:
        # fallback: render the detail directly
        return render(request, 'events/event_detail.html', {'event': event})

