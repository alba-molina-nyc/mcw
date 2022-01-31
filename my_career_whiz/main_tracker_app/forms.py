from django import forms
from django.forms import ModelForm
from .models import AppTracker, Contact

class AppTrackerForm(ModelForm):
    class Meta: 
        model = AppTracker
        fields = '__all__' 
# Creating a form to add an application
form = AppTrackerForm()

# Creating a form to change an existing application
app = AppTracker.objects.get(pk=1)
form = AppTrackerForm(instance=app)


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

form = ContactForm()

# Creating a form to change an existing application
app = Contact.objects.get(pk=1)
form = ContactForm(instance=app)

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