from django.shortcuts import render
from .models import Event
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'events'
    
    def get_queryset(self):
        return Event.objects.all()
 
class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'

def create_event(request): 
    if request.method == 'POST':
        event_title = request.POST.get('title')
        if event_title:
            Event.objects.create(name=event_title)
            return render(request, 'events/create_event.html', {'success_message': 'Event created successfully!'})
        else:
            return render(request, 'events/create_event.html', {'error_message': 'Event name cannot be empty.'})
    return render(request, 'events/create_event.html')