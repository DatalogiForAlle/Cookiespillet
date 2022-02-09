from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from .forms import StudentForm
from .models import Game, Student


def add_context_for_join_form(context, request):
    """Helper function used by view functions below"""

    # If the client has already joined a market
    if "student_id" in request.session:

        # If trader is in database
        if Student.objects.filter(id=request.session["student_id"]).exists():
            student = Student.objects.get(id=request.session["student_id"])
            # If trader has been removed from market
            if student.removed_from_market:
                request.session["removed_from_game"] = True

        # If trader has been deleted from database
        else:
            request.session["removed_from_game"] = True

        # We add this market to the context to notify the client
        game = get_object_or_404(Game, game_id=request.session["game_id"])
        context["game"] = game
    return context


@require_GET
def home(request):
    # If the client is following an invitation link to a market
    if "market_id" in request.GET:
        # Fill out the market_id field in the form
        form = StudentForm(initial={"game_id": request.GET["game_id"]})

    # If the client is just visiting the home-page base url
    else:
        # The form should be empty
        form = StudentForm()

    context = add_context_for_join_form({"form": form}, request)
    return render(request, "home.html", context)
    # return render(request, "home.html")


@login_required(redirect_field_name="home")
def create_game(request):
    new_game = Game.objects.create()
    new_game.created_by = request.user
    new_game.save()

    return redirect(reverse("monitor", args=(new_game.game_id,)))


def monitor(request, game_id):
    game = get_object_or_404(Game, game_id=game_id)

    context = {"game_id": game_id}

    return render(request, "monitor.html", context)


def play(request, game_id):
    game = get_object_or_404(Game, game_id=game_id)

    context = {"game_id": game_id}

    return render(request, "play.html", context)


@require_POST
def join_game(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        game = Game.objects.get(game_id=form.cleaned_data["game_id"])

        new_student = form.save(commit=False)
        new_student.game = game
        # new_student.balance = game.initial_balance
        # new_student.round_joined = game.round
        new_student.save()

        request.session["student_id"] = new_student.pk
        request.session["username"] = form.cleaned_data["name"]
        request.session["game_id"] = form.cleaned_data["game_id"]

        ## If player joins a game in round n>0, create 'forced trades' for round 0,1,..,n-1
        # if game.round > 0:
        #    for round_num in range(game.round):
        #        create_forced_trade(
        #            trader=new_player, round_num=round_num, is_new_player=True
        #        )

        # After joining the game, the player is redirected to the play page
        return redirect(reverse("play", args=(game.game_id,)))

    context = add_context_for_join_form({"form": form}, request)
    return render(request, "game/home.html", context)
