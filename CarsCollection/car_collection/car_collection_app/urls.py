from django.urls import path, include
from car_collection.car_collection_app.views import index, catalogue_page, car_create, car_details, car_edit, \
    car_delete, profile_create, profile_details, profile_edit, profile_delete


urlpatterns = [
    path('', index, name='home page'),
    path('catalogue/', catalogue_page, name='catalogue'),
    path('car/', include([
        path('create/', car_create, name='car create'),
        path('<int:pk>/details/', car_details, name='car details'),
        path('<int:pk>/edit/', car_edit, name='car edit'),
        path('<int:pk>/delete/', car_delete, name='car delete'),
    ])),
    path('profile/', include([
        path('create/', profile_create, name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ])),
]
