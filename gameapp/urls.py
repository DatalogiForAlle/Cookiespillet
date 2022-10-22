from django.urls import path

# from .views import HomePageView
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("my_games/", views.my_games, name="my_games"),
    path("cookie_overview/", views.cookie_overview, name="cookie_overview"),
    path(
        "<game_id>/cookie_error_overview/",
        views.cookie_error_overview,
        name="cookie_error_overview",
    ),
    path("<game_id>/cookieTester/", views.cookieTester, name="cookieTester"),
    path("create_game/", views.create_game, name="create_game"),
    path("join_game/", views.join_game, name="join_game"),
    path("<game_id>/monitor/", views.monitor, name="monitor"),
    path("<game_id>/student_table/", views.student_table, name="student_table"),
    path("<game_id>/play/", views.play, name="play"),
    path(r"delete-entry/(<pk>\d+)/", views.DeleteView.as_view(), name="delete_view"),
    ##Cookies:
    path("<game_id>/cookie0/", views.cookie0, name="cookie0"),
    path("<game_id>/cookieX/", views.cookieX, name="cookieX"),
    path(
        "<game_id>/cookie_end_screen/",
        views.cookie_end_screen,
        name="cookie_end_screen",
    ),
    path("display_test/", views.display_test, name="display_test"),
    path("<game_id>/display1/", views.display1, name="display1"),
    path("<game_id>/display2/", views.display2, name="display2"),
    path("<game_id>/display3/", views.display3, name="display3"),
    path("<game_id>/display4/", views.display4, name="display4"),
    path("<game_id>/display5/", views.display5, name="display5"),
    path("<game_id>/display6/", views.display6, name="display6"),
    path("<game_id>/display7/", views.display7, name="display7"),
    path("<game_id>/display8/", views.display8, name="display8"),
    path("<game_id>/display9/", views.display9, name="display9"),
    path("<game_id>/display10/", views.display10, name="display10"),
    path("<game_id>/display11/", views.display11, name="display11"),
    path("<game_id>/display12/", views.display12, name="display12"),
    path("<game_id>/display13/", views.display13, name="display13"),
    path("<game_id>/display14/", views.display14, name="display14"),
]
