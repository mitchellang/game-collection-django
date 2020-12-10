from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('collection/', views.GameCollectionListView.as_view(), name = 'game-collection'),
    path('collection/<uuid:pk>', views.GameCollectionDetailView.as_view(), name = 'game-collection-detail'),
]

urlpatterns += [
    path('mycollection/', views.OwnedGamesByUserListView.as_view(), name='my-collection')
]

# Add Remove collections
urlpatterns += [
    path('collection/create/', views.GameCollectionCreate.as_view(), name='game-collection-create'),
    path('collection/<uuid:pk>/update/', views.GameCollectionUpdate.as_view(), name='game-collection-update'),
    path('collection/<uuid:pk>/delete/', views.GameCollectionDelete.as_view(), name='game-collection-delete'),
    ]

urlpatterns += [
    path('collection/<uuid:pk>/create/', views.GameCreate.as_view(), name='game-create'),
    path('collection/<uuid:pk>/update/', views.GameUpdate.as_view(), name='game-update'),
    path('collection/<uuid:pk>/delete/', views.GameDelete.as_view(), name='game-delete'),
    ]
