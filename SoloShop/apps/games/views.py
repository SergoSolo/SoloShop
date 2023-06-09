from django.shortcuts import get_object_or_404, render

from .models import Game
from .utils import pages


def index(request):
    products = Game.objects.all()
    page_objects = pages(request, products, 10)
    context = {
        "products": page_objects
    }
    template = "index.html"
    return render(request, template, context)


def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    template = "detail.html"
    genres = ", ".join(game.genre.values_list('name', flat=True))
    context = {
        'game': game,
        'genres': genres
    }
    return render(request, template, context)
