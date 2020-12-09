from django.shortcuts import render

# Create your views here.

from game_catalogue.models import GameCollection, Game
from django.views import generic


def index(request):
    """View function for home page of site."""

    # Number of collections
    num_collections = GameCollection.objects.all().count()
    num_games = Game.objects.all().count()

    context = {
        'num_collections': num_collections,
        'num_games': num_games,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context = context)


class GameListView(generic.ListView):
    model = Game
    paginate_by = 10


class GameDetailView(generic.DetailView):
    model = Game
