from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .forms import AppTrackerForm
from .models import AppTracker, Contact
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# Create your views here.
def home(request):
    return render(request, 'home.html')

class AppTrackerIndex(ListView):
    model = AppTracker
    template_name = 'apps/index.html'

class AppsCreate(CreateView): 
    model = AppTracker
    template_name = 'apps/app_form.html'
    fields = '__all__'
    success_url = '/applications/'


class ContactList(ListView):
    model = Contact
    template_name = 'contacts/index.html'

class ContactsCreate(CreateView): 
    model = Contact
    template_name = 'contacts/contact_form.html'
    fields = '__all__'
    success_url = '/contacts/'

#  def applications_index(request): 
#     model: AppTracker.objects.all()
#     template_name = 'apps/index.html'
#     return render(request, 'apps/index.html')
