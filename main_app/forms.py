from django import forms
from .models import Visa

class VisaForm(forms.ModelForm):
    class Meta:
        model = Visa
        fields = ['full_name', 'passport_number', 'destination_country', 'travel_date', 'status']
        widgets = {'travel_date': forms.DateInput(attrs={'type': 'date'})}

