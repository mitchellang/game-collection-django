from django.db import models

# Create your models here.

from django.urls import reverse
from django.contrib.auth.models import User
import uuid  # Required for unique book instances
from datetime import date


class GameCollection(models.Model):
    """Model representing a Game Collection genre."""
    collection_id = models.UUIDField(primary_key = True,  default = uuid.uuid4,
                                     help_text = "Unique collection identifier Id")
    collection_name = models.CharField(max_length = 200, help_text = 'Name of game collection')
    collection_created_date = models.DateField(null = True, blank = True, default=date.today)
    collection_description = models.TextField(max_length = 2000)
    owner = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)

    def get_absolute_url(self):
        return reverse('game-collection-detail', args=[str(self.collection_id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.collection_name


class Game(models.Model):
    """Model representing an author."""
    game_id = models.UUIDField(primary_key = True,  default = uuid.uuid4,
                               help_text = "Unique game identifier Id")
    game_title = models.CharField(max_length=100)
    game_description = models.TextField(max_length=2000)
    game_category = models.CharField(max_length=200, null=True, default=None)
    game_rule = models.TextField(max_length=2000)
    game_created_date = models.DateField(null=True, blank=True,default=date.today)
    game_collection = models.ManyToManyField(GameCollection, help_text = "Game collection Game belongs to")

    RATING_CHOICES = (
        (1, "Very Bad"),
        (2, "Bad"),
        (3, "Neutral"),
        (4, "Good"),
        (5, "Very Good")
    )

    game_rating = models.IntegerField(choices = RATING_CHOICES, null=True)

    def get_absolute_url(self):
        return reverse('game-detail', args=[str(self.game_id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.game_id, self.game_title)



