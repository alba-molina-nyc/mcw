from django.db import models

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
    

