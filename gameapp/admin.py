from django.contrib import admin

from .models import Game, Student, Result

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = (
        "game_id",
        "game_started",
        "created_at",
        "created_by",
        "errors_cookie_1",
        "errors_cookie_2",
        "errors_cookie_3",
        "errors_cookie_4",
        "errors_cookie_5",
        "errors_cookie_6",
        "errors_cookie_7",
        "errors_cookie_8",
        "errors_cookie_9",
        "errors_cookie_10",
        "errors_cookie_11",
    )


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "game",
        "name",
        "score",
        "correct_cookies",
        "start_time",
        "time_spent",
    )


# class ResultAdmin(admin.ModelAdmin):
#    list_display = ("student",)


admin.site.register(Game, GameAdmin)
admin.site.register(Student, StudentAdmin)
# admin.site.register(Result, ResultAdmin)
