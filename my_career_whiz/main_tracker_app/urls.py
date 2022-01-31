from django.urls import path
from . import  views

app_name = 'main_tracker_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('applications/', views.AppTrackerIndex.as_view(), name='index'),
    path('applications/create/', views.AppsCreate.as_view(), name='apps_create'),
    # path('applications/', views.applications_index, name='index'),

# define all app-level URLS in this list

]