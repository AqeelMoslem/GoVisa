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
        fields = ['receiver', 'subject', 'body']

        

class VisaStatusForm(forms.ModelForm):
    class Meta:
        model = Visa
        fields = ['status']  # بس الحالة تتغير (والملف نرفعه يدوي في view)