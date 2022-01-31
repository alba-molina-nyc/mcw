from django import forms
from django.forms import ModelForm
from .models import AppTracker

class AppTrackerForm(ModelForm):
    class Meta: 
        model = AppTracker
        fields = '__all__' 
# Creating a form to add an application
form = AppTrackerForm()

# Creating a form to change an existing application
app = AppTracker.objects.get(pk=1)
form = AppTrackerForm(instance=app)


# [
#             'jobpost_title',
#             'company_name',
#             'company_website',
#             'job_title',
#             'salary',
#             'jobpost_url',
#             'applied',
#             'office_location',
#             'app_status'
#         ]