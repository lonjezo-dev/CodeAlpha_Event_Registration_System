
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Registration
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


# Create your views here.
@login_required(login_url='accounts:login')
def index(request):
    events = Event.objects.all()
    # compute a boolean to avoid re-evaluating the queryset inside the template
    no_events = not events.exists()

    # get logged in user 
    user = request.user

    # get user's registrations
    user_registrations = Registration.objects.filter(user=user).select_related('event')

    context ={
        'user': user,
        'events': events,
        'no_events': no_events,
        'user_registrations': user_registrations,
    }
    return render(request, 'events/index.html', context)


def detail(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        return render(request, 'events/event_detail.html', {'error_message': 'Event not found.'})
    return render(request, 'events/event_detail.html', {'event': event})


@login_required(login_url='accounts:login')
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
        # messages.success(request, 'You have successfully registered for this event.')
        return redirect('events:index')
    else:
        messages.info(request, 'You are already registered for this event.')
        

    # Redirect back to the event detail page using the app namespace
    try:
        return redirect('events:detail', event_id=event.id)
    except Exception:
        # fallback: render the detail directly
        return render(request, 'events/event_detail.html', {'event': event})



@login_required(login_url='accounts:login')
@require_POST
def cancel(request, event_id):
    try:
        registration= Registration.objects.get(user=request.user, event_id=event_id)
        registration.delete()
        # messages.success(request, "You have successfully cancelled your registration.")
    except Registration.DoesNotExist:
        messages.warning(request, "You were not registered for this event.")

    return redirect('events:index')
