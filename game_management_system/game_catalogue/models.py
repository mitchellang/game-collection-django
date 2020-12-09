from django.db import models

# Create your models here.

from django.urls import reverse
import uuid  # Required for unique book instances
from datetime import date


class Game(models.Model):
    """Model representing an author."""
    game_title = models.CharField(max_length=100)
    game_description = models.TextField(max_length=2000)
    game_category = models.TextField(max_length=2000)
    game_rule = models.TextField(max_length=2000)
    game_created_date = models.DateField(null=True, blank=True)

    RATING_CHOICES = (
        (1, "Very Bad"),
        (2, "Bad"),
        (3, "Neutral"),
        (4, "Good"),
        (5, "Very Good")
    )

    game_rating = models.IntegerField(choices = RATING_CHOICES)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('game-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.game_title


class GameCollection(models.Model):
    """Model representing a book genre."""
    collection_name = models.CharField(max_length = 200, help_text = 'Name of game collection')
    collection_created_date = models.DateField(null = True, blank = True)
    collection_description = models.TextField(max_length = 2000)
    collection_games = models.ForeignKey("Game", on_delete = models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.collection_name
