from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:event_id>/', views.detail, name='detail'),
    path('create/', views.create_event, name='create_event'),
]