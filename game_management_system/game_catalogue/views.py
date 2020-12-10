from django.shortcuts import render

# Create your views here.

from game_catalogue.models import GameCollection, Game
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    """View function for home page of site."""

    # Number of collections
    num_collections = GameCollection.objects.filter(owner = request.user).count()
    num_games = Game.objects.filter(game_collection__owner = request.user).count()

    context = {
        'num_collections': num_collections,
        'num_games': num_games,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context = context)


class GameCollectionListView(generic.ListView):
    model = GameCollection
    paginate_by = 10


class GameCollectionDetailView(generic.DetailView):
    model = GameCollection


class OwnedGamesByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = GameCollection
    template_name = 'game_catalogue/gamecollection_list_owned_user.html'
    paginate_by = 10

    def get_queryset(self):
        return GameCollection.objects.filter(owner = self.request.user)

