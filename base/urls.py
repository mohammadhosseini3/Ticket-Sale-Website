from django.urls import path
from . import views

app_name = 'concert_app'
urlpatterns = [
    path('concert_list/',views.concertListView,name='concert_list'),
    path('location_list/',views.locationListView,name='location_list'),
    path('concert/<int:pk>',views.detailView,name='detail'),
    path('time_list/',views.timeListView,name='time_list'),
    path('concert_editing/<int:pk>',views.concertEditing,name='concert_editing'),
]
