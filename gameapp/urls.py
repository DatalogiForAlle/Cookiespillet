from django.urls import path
from .views import HomePageView
from . import views

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("create_game/", views.create_game, name="create_game"),
]
