from django.db import models
from django.contrib.auth import get_user_model


class Game(models.Model):
    context_object_name = "Game"
    game = models.CharField(max_length=16, primary_key=True)
    # creator_id  # Hører til den Lærer/Account som har oprettet spillet.
    game_over = models.BooleanField(default=False)

    # def check_game_over(self):
    #    """
    #    Checks if the game state should be set to game_over.
    #    """
    #    if (no time left...):
    #        return True

    # created_at = models.DateTimeField(auto_now_add=True, null=True)
    # created_by = models.ForeignKey(
    #    get_user_model(), null=True, on_delete=models.SET_NULL
    # )


class Student(models.Model):
    context_object_name = "Student"
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    score = models.IntegerField()

    # Nice to have, lærer skal kunne fjerne spillere med upassende navne
    # removed_from_game = models.BooleanField(default=False)


class Result(models.Model):
    context_object_name = "Results"
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # cookie_number
    # point
    # time
