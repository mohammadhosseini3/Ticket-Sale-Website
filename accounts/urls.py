from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout'),
    path('profile/',views.profileView,name='profile'),
    path('regsiter/',views.registerView,name='register'),
    path('edit_profile/',views.ProfileEditView,name='edit_profile'),
]