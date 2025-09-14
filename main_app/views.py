# main_app/views.py

from django.shortcuts import render, redirect

# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import HttpResponse to send text-based responses
from django.http import HttpResponse
from .models import Visa 
# from .forms import FeedingForm

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
    visas = Visa.objects.filter(user=request.user)
    return render(request, 'visas/index.html', { 'visas': visas })

