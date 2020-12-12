from django.shortcuts import render

# Create your views here.

from game_catalogue.models import GameCollection, Game
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
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


class GameCollectionDetailView(generic.DetailView):
    model = GameCollection

    def get_context_data(self, **kwargs):
        context = super(GameCollectionDetailView, self).get_context_data(**kwargs)
        collection = self.get_object()
        try:
            a = self.request.GET.get('game_name', )
        except KeyError:
            a = None
        if a or a != "":
            context['filtered_games'] = Game.objects.filter(game_collection = collection,
                                                            game_title__contains = a)
        else:
            context['filtered_games'] = Game.objects.filter(game_collection = collection)
        return context


class OwnedGamesByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = GameCollection
    template_name = 'game_catalogue/gamecollection_list_owned_user.html'
    paginate_by = 10

    def get_queryset(self):
        return GameCollection.objects.filter(owner = self.request.user)


class GameDetailView(generic.DetailView):
    model = Game


class GameCollectionCreate(CreateView):
    model = GameCollection
    fields = ['collection_name', 'collection_description']

    def form_valid(self, form):
        owner = self.request.user
        form.instance.owner = owner
        return super(GameCollectionCreate, self).form_valid(form)


class GameCollectionUpdate(UpdateView):
    model = GameCollection
    fields = ['collection_name', 'collection_description']


class GameCollectionDelete(DeleteView):
    model = GameCollection
    success_url = reverse_lazy('my-collection')


class GameCreate(CreateView):
    model = Game
    fields = ['game_title', 'game_description', 'game_rule', 'game_created_date', 'game_category',
              'game_rating']

    def get_initial(self):
        return {"game_collection": self.kwargs.get("pk")}

    def get_success_url(self):
        return reverse('game-collection-detail', args=[str(self.get_initial()['game_collection'])])

    def form_valid(self, form):
        owner = self.request.user
        form.instance.owner = owner
        form.save()
        game_collection = GameCollection.objects.get(collection_id=str(self.get_initial()['game_collection']))
        form.instance.game_collection.set([game_collection])
        return super(GameCreate, self).form_valid(form)


class GameUpdate(UpdateView):
    model = Game
    fields = ['game_title', 'game_description', 'game_rule', 'game_created_date', 'game_category',
              'game_rating']


class GameDelete(DeleteView):
    model = Game
    success_url = reverse_lazy('my-collection')
