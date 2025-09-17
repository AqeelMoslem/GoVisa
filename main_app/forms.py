from django import forms
from .models import Visa, Message
from django.contrib.auth.models import User

class VisaForm(forms.ModelForm):
    class Meta:
        model = Visa
        fields = ['full_name', 'passport_number', 'destination_country', 'travel_date']
        widgets = {'travel_date': forms.DateInput(attrs={'type': 'date'})}


class MessageForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(queryset=User.objects.none(), label="To")

    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            if user.is_staff:
                # Admin can send to any user except themselves
                self.fields['receiver'].queryset = User.objects.exclude(id=user.id)
            else:
                # Normal user can send only to admins, not themselves
                self.fields['receiver'].queryset = User.objects.filter(is_staff=True).exclude(id=user.id)

                
class VisaStatusForm(forms.ModelForm):
    class Meta:
        model = Visa
        fields = ['status']
