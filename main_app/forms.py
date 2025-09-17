from django import forms
from .models import Visa, Message
from django.contrib.auth.models import User

class VisaForm(forms.ModelForm):
    class Meta:
        model = Visa
        fields = ['full_name', 'passport_number', 'destination_country', 'travel_date', 'status']
        widgets = {'travel_date': forms.DateInput(attrs={'type': 'date'})}


class MessageForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(queryset=User.objects.all(), label="To")

    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['receiver'].queryset = User.objects.filter(is_staff=True) | User.objects.filter(is_superuser=True)


class VisaStatusForm(forms.ModelForm):
    class Meta:
        model = Visa
        fields = ['status']
