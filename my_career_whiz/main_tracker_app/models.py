from statistics import mode
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



# Create your models here.

class AppTracker(models.Model):
    APP_STATUS = (
        ('SA', 'Submitted Application' ),
        ('SI', 'Scheduled Interview'),
        ('RO', 'Received Offer'),
        ('NS', 'Negotiation State'),
        ('NO', 'No Offer'),
        ('RC', 'Reference Check'),
    )
    LOCATION = (
        ('R', 'Remote'),
        ('H', 'Hybrid'),
        ('I', 'In Office'),
    )
    jobpost_title = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    company_website = models.URLField(max_length=250)
    job_title = models.CharField(max_length=250)
    salary = models.CharField(max_length=250)
    jobpost_url = models.URLField(max_length=200)
    applied = models.BooleanField(default=False)
    office_location = models.CharField(max_length=200)
    job_location = models.CharField(
        max_length=1,
        choices=LOCATION)
    app_status =  models.CharField(
        max_length=2,
        choices=APP_STATUS)

    
    def __str__(self):
        return self.job_title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'app_id': self.id})


class Contact(models.Model): 
    CONTACT_STATUS = (
        ('LR', 'Sent LinkedIn Request'),
        ('LM', 'Sent LinkedIn Message'),
        ('GI', 'Got an intro'),
        ('SI', 'Scheduled Interview'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=75)
    company_name = models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    linkedin = models.URLField(max_length=200)
    status = models.CharField(
        max_length=2,
        choices=CONTACT_STATUS)

    
    
 
    
  

