from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .forms import GameForm


class HomePageView(TemplateView):
    template_name = "home.html"


# class StartGameView(TemplateView):
#    template_name = "start_game.html"


@login_required(redirect_field_name="home")
def create_game(request):
    form = GameForm()
    # if form.is_valid():
    new_game = form.save(commit=False)
    new_game.created_by = request.user
    new_game.save()

    return render(request, "create_game.html")
