from django.urls import path
from Notes.notes_app.views import index, create_note, edit_note, delete_note, details_note, \
    delete_profile, user_profile

urlpatterns = [
    path('', index, name='home page'),
    path('add/', create_note, name='create note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', details_note, name='details note'),
    path('profile/', user_profile, name='user profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]
