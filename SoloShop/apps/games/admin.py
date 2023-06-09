from django.contrib import admin

from .models import Game, Genre


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ["name", "developer", "price", "release_date"]
    list_filter = ["developer", "publisher", "price"]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
