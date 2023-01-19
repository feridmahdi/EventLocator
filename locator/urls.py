from django.urls import path
from locator import views

urlpatterns = [
    path("", views.home, name="home"),
    path("locator/<name>", views.hello_there, name="hello_there"),
    path("map", views.map_view, name="map"),
    path("calendar/", views.CalendarView.as_view(), name="calendar"),
    path("event/new/", views.event, name="event_new"),
    path("event/edit/(<event_id>\d+)/", views.event, name="event_edit"),
]