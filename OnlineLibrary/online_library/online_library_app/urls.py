from django.urls import path, include
from online_library.online_library_app.views import index, add_book, edit_book, details_book, \
    profile, edit_profile, delete_profile, delete_book

urlpatterns = [
    path('', index, name='home page'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('details/<int:pk>/', details_book, name='details book'),
    path('delete/<int:pk>/', delete_book, name='delete book'),
    path('profile/', include([
        path('', profile, name='profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ]))
]
