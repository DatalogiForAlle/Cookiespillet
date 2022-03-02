from dataclasses import field
from django import forms
from .models import Game, Student


class StudentForm(forms.ModelForm):
    game_id = forms.CharField(
        max_length=16,
        label="Spil-ID",
        help_text="Indtast ID'et på det spil, du vil deltage i.",
    )

    class Meta:
        model = Student
        fields = ["name"]
        labels = {
            "name": "Navn",
        }
        help_texts = {
            "name": "Navnet, du vælger her, vil være synligt for de andre deltagere i spillet.",
        }

    def clean_game_id(self):
        """Additional validation of the form's game_id field"""
        game_id = self.cleaned_data["game_id"].upper()

        if not Game.objects.filter(pk=game_id).exists():
            raise forms.ValidationError("Der er intet spil med dette ID.")
        return game_id

    def clean(self):
        """
        Additional validation of form data:
        Validate that there are no other users on the market with the chosen username
        """
        cleaned_data = super().clean()
        cleaned_name = cleaned_data.get("name")
        cleaned_game_id = cleaned_data.get("game_id")
        if cleaned_name and cleaned_game_id:
            game = Game.objects.get(game_id=cleaned_game_id)
            # if game.game_over:
            #    raise forms.ValidationError(
            #        "Dette spil er afsluttet. Ingen nye spillere kan deltage."
            #    )

            if Student.objects.filter(name=cleaned_name, game=game).exists():
                raise forms.ValidationError(
                    "Der er allerede en spiller med dette navn. Vælg et andet navn."
                )

        return cleaned_data
