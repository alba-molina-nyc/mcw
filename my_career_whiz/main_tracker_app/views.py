from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import AppTracker

# Create your views here.
def home(request):
    return render(request, 'home.html')

class AppTrackerIndex(ListView):
    model = AppTracker
    template_name = 'apps/index.html'


# def applications_index(request): 
#     model: AppTracker.objects.all()
#     template_name = 'apps/index.html'
#     return render(request, 'apps/index.html')
