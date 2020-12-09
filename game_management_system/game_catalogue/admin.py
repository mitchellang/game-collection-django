from django.contrib import admin

# Register your models here.

from .models import Game, GameCollection

admin.site.register(Game)
admin.site.register(GameCollection)
