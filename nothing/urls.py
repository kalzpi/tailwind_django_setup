from django.urls import path
from . import views


app_name = "nothing"

urlpatterns = [
    path("", views.HomeView, name="home"),
]