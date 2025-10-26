from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('/<int:event_id>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.create_event, name='create_event'),
]