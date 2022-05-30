from datetime import datetime, timezone
from django.urls import reverse, reverse_lazy
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    HttpResponseRedirect,
)
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
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

        # We add this market to the context to notify the client
        game = get_object_or_404(Game, game_id=request.session["game_id"])
        context["game"] = game
    return context


@require_GET
def home(request):
    # If the client is following an invitation link to a market
    if "game_id" in request.GET:
        # Fill out the market_id field in the form
        form = StudentForm(initial={"game_id": request.GET["game_id"]})

    # If the client is just visiting the home-page base url
    else:
        # The form should be empty
        form = StudentForm()

    context = add_context_for_join_form({"form": form}, request)
    return render(request, "home.html", context)


@login_required(redirect_field_name="home")
def create_game(request):
    new_game = Game.objects.create()
    new_game.created_by = request.user
    new_game.save()

    return redirect(reverse("monitor", args=(new_game.game_id,)))


def monitor(request, game_id):
    game = get_object_or_404(Game, game_id=game_id)
    try:
        flag = int(request.POST["flag"])
        if flag == 1:
            game.game_started = True
            game.save()
    except KeyError:
        print("Where is my flag?")

    # Only the user who created the market has permission to monitor page
    if not request.user == game.created_by:
        return HttpResponseRedirect(reverse("home"))

    context = {
        "game": game,
        "game_id": game_id,
    }
    return render(request, "monitor.html", context)


def play(request, game_id):
    game = get_object_or_404(Game, game_id=game_id)
    try:
        student = Student.objects.get(id=request.session["student_id"])
    except:
        # if not trader in session return to home:
        return redirect(reverse("home"))

    context = {
        "game_id": game_id,
        "student_name": student.name,
    }
    if game.game_started == True:
        return redirect(reverse("cookie0", args=(game_id,)), context)

    return render(request, "play.html", context)


@require_POST
def join_game(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        game = Game.objects.get(game_id=form.cleaned_data["game_id"])

        new_student = form.save(commit=False)
        new_student.game = game
        new_student.score = 0
        new_student.save()

        request.session["student_id"] = new_student.pk
        request.session["username"] = form.cleaned_data["name"]
        request.session["game_id"] = form.cleaned_data["game_id"]

        # After joining the game, the player is redirected to the play page
        return redirect(reverse("play", args=(game.game_id,)))

    context = add_context_for_join_form({"form": form}, request)
    return render(request, "home.html", context)


@require_GET
# @login_required
def student_table(request, game_id):
    game = get_object_or_404(Game, game_id=game_id)

    # If user is not the creator of the game, redirect to home page
    # if not request.user == game.created_by:
    #    return HttpResponseRedirect(reverse("home"))

    return render(request, "student_table.html", {"game": game})


class DeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy("monitor")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = self.object.name
        request.session["name"] = name  # name will be change according to your need
        return super(DeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("monitor", kwargs={"game_id": self.object.game_id})


def update_score(student):
    student.time_spent = round(student.calculate_time_spent(), 2)
    student.score = (
        student.correct_cookies * 1000
        - student.time_spent * 100
        - student.wrong_cookies * 50
    )
    student.save()


def cookie0(request, game_id):
    try:
        student = Student.objects.get(id=request.session["student_id"])
    except:
        # if not trader in session return to home:
        return redirect(reverse("home"))

    if student.current_cookie == 0:
        student.start_time = datetime.now(timezone.utc)
        student.current_cookie += 1
        student.save()

        context = {
            "student_name": student.name,
            "game_id": game_id,
        }
        return render(request, "cookies/cookie0.html", context)
    else:
        return reverse("home")


def cookieX(request, game_id):
    game = get_object_or_404(Game, game_id=game_id)

    try:
        student = Student.objects.get(id=request.session["student_id"])
    except:
        # if not student in session return to home:
        return redirect(reverse("home"))

    try:
        flag = int(request.POST["flag"])
        if flag == 1:
            student.correct_cookies += 1
        else:
            student.wrong_cookies += 1
        update_total_errors(student.current_cookie, game)
    except KeyError:
        print("Where is my flag?")

    context = {
        "student_name": student.name,
        "game_id": game_id,
    }
    template = "cookies/cookie" + str(student.current_cookie) + ".html"
    student.current_cookie += 1
    update_score(student)
    return render(request, template, context)


def cookie_end_screen(request, game_id):
    game = get_object_or_404(Game, game_id=game_id)
    try:
        flag = int(request.POST["flag"])
        if flag == 1:
            game.game_started = True
            game.save()
    except KeyError:
        print("Where is my flag?")

    try:
        student = Student.objects.get(id=request.session["student_id"])
    except:
        # if not student in session return to home:
        return redirect(reverse("home"))

    try:
        flag = int(request.POST["flag"])
        if flag == 1:
            student.correct_cookies += 1
        else:
            student.wrong_cookies += 1
            update_total_errors(student.current_cookie, game)
    except KeyError:
        print("Where is my flag?")

    context = {
        "student_name": student.name,
        "game": game,
        # "game_id": game_id,
    }

    update_score(student)
    return render(request, "cookies/cookie_end_screen.html", context)


@login_required
def cookie_overview(request):
    return render(request, "cookies/cookie_overview.html")


@login_required
def cookie_error_overview(request, game_id):
    game = get_object_or_404(Game, game_id=game_id)
    context = {
        "game_id": game_id,
        "errors1": game.errors_cookie_1,
        "errors2": game.errors_cookie_2,
        "errors3": game.errors_cookie_3,
        "errors4": game.errors_cookie_4,
        "errors5": game.errors_cookie_5,
        "errors6": game.errors_cookie_6,
        "errors7": game.errors_cookie_7,
        "errors8": game.errors_cookie_8,
        "errors9": game.errors_cookie_9,
        "errors10": game.errors_cookie_10,
        "errors11": game.errors_cookie_11,
    }
    return render(request, "cookie_error_overview.html", context)


def cookieTester(request, game_id):

    context = {
        "game_id": game_id,
    }

    return render(request, "cookies/cookieTester.html", context)


def update_total_errors(current_cookie, game):
    temp = current_cookie - 1
    if (
        (temp) == 0
        or (temp) == 1
        or (temp) == 5
        or (temp) == 8
        or (temp) == 10
        or (temp) == 20
        or (temp) == 23
        or (temp) == 31
        or (temp) == 49
        or (temp) == 56
    ):
        game.errors_cookie_1 += 1
    elif (
        (temp) == 2
        or (temp) == 4
        or (temp) == 9
        or (temp) == 15
        or (temp) == 18
        or (temp) == 22
        or (temp) == 26
        or (temp) == 45
    ):
        game.errors_cookie_2 += 1
    elif (
        (temp) == 3
        or (temp) == 6
        or (temp) == 11
        or (temp) == 13
        or (temp) == 21
        or (temp) == 32
        or (temp) == 33
        or (temp) == 35
        or (temp) == 36
        or (temp) == 39
        or (temp) == 44
    ):
        game.errors_cookie_3 += 1
    elif (
        (temp) == 7
        or (temp) == 12
        or (temp) == 19
        or (temp) == 25
        or (temp) == 30
        or (temp) == 34
        or (temp) == 38
        or (temp) == 53
    ):
        game.errors_cookie_4 += 1
    elif (
        (temp) == 16
        or (temp) == 17
        or (temp) == 24
        or (temp) == 27
        or (temp) == 37
        or (temp) == 42
    ):
        game.errors_cookie_5 += 1
    elif (temp) == 14 or (temp) == 40 or (temp) == 52:
        game.errors_cookie_6 += 1
    elif (temp) == 28 or (temp) == 41 or (temp) == 46:
        game.errors_cookie_7 += 1
    elif (temp) == 29 or (temp) == 43 or (temp) == 48 or (temp) == 55:
        game.errors_cookie_8 += 1
    elif (temp) == 47 or (temp) == 51:
        game.errors_cookie_9 += 1
    elif (temp) == 50 or (temp) == 54:
        game.errors_cookie_10 += 1
    elif (temp) == 57:
        game.errors_cookie_11 += 1
    game.save()
