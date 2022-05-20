from django.urls import path

# from .views import HomePageView
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cookieTester", views.cookieTester, name="cookieTester"),
    path("create_game/", views.create_game, name="create_game"),
    path("join_game/", views.join_game, name="join_game"),
    path("<game_id>/monitor/", views.monitor, name="monitor"),
    path("<game_id>/student_table/", views.student_table, name="student_table"),
    path("<game_id>/play/", views.play, name="play"),
    path(r"delete-entry/(<pk>\d+)/", views.DeleteView.as_view(), name="delete_view"),
    ##Cookies:
    path("cookie0/", views.cookie0, name="cookie0"),
    path("cookieX/", views.cookieX, name="cookieX"),
    path(
        "<game_id>/cookie_end_screen/",
        views.cookie_end_screen,
        name="cookie_end_screen",
    ),
]
