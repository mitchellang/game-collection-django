from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.GameCollectionListView.as_view(), name = 'game-collection'),
    path('games/<uuid:pk>', views.GameCollectionDetailView.as_view(), name = 'game-collection-detail'),
]

urlpatterns += [
    path('mycollection/', views.OwnedGamesByUserListView.as_view(), name='my-collection')
]
