from django.urls import path
from locator import views

urlpatterns = [
    path("", views.home, name="home"),
    path("locator/<name>", views.hello_there, name="hello_there"),
]