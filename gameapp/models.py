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
    game_over = models.BooleanField(default=False)

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


class Student(models.Model):
    context_object_name = "Student"
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    score = models.IntegerField()

    # Nice to have, lærer skal kunne fjerne spillere med upassende navne
    removed_from_game = models.BooleanField(default=False)


class Result(models.Model):
    context_object_name = "Results"
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # cookie_number = models
    # point
    # time
