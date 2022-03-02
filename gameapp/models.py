from django.utils.timezone import utc
from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string


def new_unique_game_id():
    """
    Create a new unique game ID (8 alphabetic chars)
    """
    while True:
        game_id = get_random_string(8, allowed_chars="ABCDEFGHIJKLMSOPQRSTUVXYZ")
        if not Game.objects.filter(game_id=game_id).exists():
            break
    return game_id


class Game(models.Model):
    context_object_name = "Game"
    game_id = models.CharField(max_length=16, primary_key=True)
    # creator_id  # Hører til den Lærer/Account som har oprettet spillet.
    game_started = models.BooleanField(default=False)

    # def check_game_over(self):
    #    """
    #    Checks if the game state should be set to game_over.
    #    """
    #    if (no time left...):
    #        return True

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.SET_NULL
    )

    def save(self, *args, **kwargs):
        """
        Do the following before creating a new game object:
            *) Set unique custom id for game
        """
        if (
            not self.game_id
        ):  # <== we are in fact creating a new game (not updating an existing game)
            self.game_id = new_unique_game_id()
        super(Game, self).save(*args, **kwargs)

    def active_students(self):
        """
        Returns a query set of all active traders on the market.
        A trader is 'active' if he has not declared bankruptcy and has not been removed from the market.
        """
        active_students = Student.objects.filter(
            game=self,
        )
        active_students = active_students.order_by("-score")
        return active_students


class Student(models.Model):
    context_object_name = "Student"
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    score = models.IntegerField()
    correct_cookies = models.IntegerField(default=0)
    wrong_cookies = models.IntegerField(default=0)
    start_time = models.DateTimeField(auto_now_add=True, blank=True)
    time_spent = models.FloatField(default=0.0)
    current_cookie = models.IntegerField(default=0)

    def calculate_time_spent(self):
        now = datetime.utcnow().replace(tzinfo=utc)
        timediff = now - self.start_time
        return timediff.total_seconds()


class Result(models.Model):
    context_object_name = "Results"
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # cookie_number = models
    # point
    # time
