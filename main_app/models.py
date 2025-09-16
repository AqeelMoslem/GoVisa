from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

class Visa(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
        ("Completed", "Completed"),
    ]
    full_name = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=50)
    destination_country = models.CharField(max_length=100)
    travel_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # document = models.FileField(upload_to="visas_docs/", null=True, blank=True)
    document = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.status}"

from django import forms
from .models import Visa

class VisaStatusForm(forms.ModelForm):
    upload_file = forms.FileField(required=False)  # خاص بحالة Completed

    class Meta:
        model = Visa
        fields = ["status"]


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    subject = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject} - from {self.sender} to {self.receiver}"
