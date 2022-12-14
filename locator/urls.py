from django.urls import path
from locator import views

urlpatterns = [
    path("", views.home, name="home"),
]