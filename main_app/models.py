from django.db import models
from django.urls import reverse


class Visa(models.Model):
    full_name = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=50)
    destination_country = models.CharField(max_length=100)
    travel_date = models.DateField()
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return f"{self.full_name} - {self.destination_country}"
    def get_absolute_url(self):
        return reverse('visa-detail', kwargs={'visa_id': self.id})
    
