from django import forms
from .models import Visa
from .models import Message


class VisaForm(forms.ModelForm):
    class Meta:
        model = Visa
        fields = ['full_name', 'passport_number', 'destination_country', 'travel_date', 'status']
        widgets = {'travel_date': forms.DateInput(attrs={'type': 'date'})}


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your message here...', 'rows': 5}),
        }