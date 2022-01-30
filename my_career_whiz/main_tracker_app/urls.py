from django.urls import path
from . import  views

app_name = 'main_tracker_app'
urlpatterns = [
# define all app-level URLS in this list
    path('', views.home, name='home'),  
]