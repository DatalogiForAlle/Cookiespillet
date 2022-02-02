from django.contrib import admin

from .models import Game, Student, Result

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = (
        "game",
        "game_over",
    )


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "game",
        "name",
        "score",
    )


class ResultAdmin(admin.ModelAdmin):
    list_display = ("student",)


admin.site.register(Game, GameAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Result, ResultAdmin)
