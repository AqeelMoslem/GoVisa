# main_app/views.py
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import HttpResponse to send text-based responses
from django.http import HttpResponse
from .models import Visa 
from .forms import VisaForm


from django.views.generic import ListView, DetailView # add these 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
# Other view functions above


# Define the home view function
def home(request):
    return render(request, 'home.html')
class Home(LoginView):
    template_name = 'home.html'



def about(request):
    return render(request, 'about.html')


def visa_index(request):
    visas = Visa.objects.all() 
    return render(request, 'visas/index.html', { 'visas': visas })

# views.py

def visa_detail(request, visa_id):
    visa = Visa.objects.get(id=visa_id)
    return render(request, 'visas/detail.html', {'visa': visa})

# main-app/views.py

class VisaCreate(CreateView):
    model = Visa
    form_class = VisaForm       # لتعديل البيانات مع calendar picker
    success_url = reverse_lazy('visa-index') 
    # def form_valid(self, form):
    #     # Assign the logged in user (self.request.user)
    #     form.instance.user = self.request.user  # form.instance is the cat
    #     # Let the CreateView do its job as usual
    #     return super().form_valid(form)

class VisaUpdate(UpdateView):
    model = Visa
    fields = ['passport_number', 'destination_country', 'travel_date']

    

class VisaDelete(DeleteView):
    model = Visa
    success_url = '/visas/'