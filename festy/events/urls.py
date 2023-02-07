from django.urls import path
from .views import (
    EventUpdateView,
    EventDeleteView
)
from . import views

urlpatterns = [
    path('', views.index, name="events-home"),
    path('ev_register/<int:pk>/',views.register, name='event-register'),
    path('registered/',views.registered, name='registered-events'),
    path('ev_create',views.ev_create, name='ev_create'),
    path('event/<pk>/', views.event_detail, name='event-detail'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
]