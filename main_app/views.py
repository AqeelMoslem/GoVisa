# main_app/views.py
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import HttpResponse to send text-based responses
from django.http import HttpResponse
from .models import Visa 
from .forms import VisaForm
# from .forms import MessageForm
from django.conf import settings

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

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm
@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'messages/inbox.html', {'messages': messages})

@login_required
def sent_messages(request):
    messages = Message.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'messages/sent.html', {'sent_messages': messages})

@login_required
def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if message.receiver == request.user:
        message.read = True
        message.save()
    return render(request, 'messages/detail.html', {'message': message})

@login_required
def new_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            return redirect('sent-messages')
    else:
        form = MessageForm()
    return render(request, 'messages/new_message.html', {'form': form})
