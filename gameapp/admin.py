from django.contrib import admin

from .models import Game, Student, Result

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = (
        "game_id",
        "game_over",
        "created_at",
        "created_by",
    )


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "game",
        "name",
        "score",
        "correct_cookies",
        "started_playing_at",
        "finished_playing_at",
    )


# class ResultAdmin(admin.ModelAdmin):
#    list_display = ("student",)


admin.site.register(Game, GameAdmin)
admin.site.register(Student, StudentAdmin)
# admin.site.register(Result, ResultAdmin)
