from django.urls import path
from locator import views

urlpatterns = [
    path("", views.home, name="home"),
    path("osmap", views.osmap, name="osmap"),
    path("calendar/", views.CalendarView.as_view(), name="calendar"),
    path("event/new/", views.event, name="event_new"),
    path("event/edit/(<event_id>\d+)/", views.event, name="event_edit"),
]