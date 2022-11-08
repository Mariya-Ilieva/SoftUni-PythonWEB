from django.urls import path, include
from GamesPlay.games_play_app.views import index, dashboard_page, game_create, game_details, game_edit, game_delete, \
    profile_create, profile_details, profile_edit, profile_delete

urlpatterns = [
    path('', index, name='home page'),
    path('dashboard/', dashboard_page, name='dashboard'),
    path('game/', include([
        path('create/', game_create, name='game create'),
        path('details/<int:pk>/', game_details, name='game details'),
        path('edit/<int:pk>/', game_edit, name='game edit'),
        path('delete/<int:pk>/', game_delete, name='game delete'),
    ])),
    path('profile/', include([
        path('create/', profile_create, name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ])),
]
