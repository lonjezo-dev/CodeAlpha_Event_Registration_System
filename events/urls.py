from django.urls import path
from . import views

# Namespacing helps reversing URLs from other apps or project-level code
app_name = 'events'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:event_id>/', views.detail, name='detail'),
    path('<int:event_id>/register/', views.register_event, name='register'),
    path('<int:event_id>/cancel/',views.cancel,name='cancel')
]