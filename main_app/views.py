# main_app/views.py
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import HttpResponse to send text-based responses
from django.http import HttpResponse
from .models import Visa 
from .forms import VisaForm
from .forms import MessageForm
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


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm
from django.conf import settings

@login_required
def inbox(request):
    # الرسائل المستلمة والمرسلة
    messages_received = Message.objects.filter(recipient=request.user).order_by('-created_at')
    messages_sent = Message.objects.filter(sender=request.user).order_by('-created_at')
    return render(request, 'inbox.html', {
        'messages_received': messages_received,
        'messages_sent': messages_sent
    })

@login_required
def send_message(request, recipient_id=None, reply_to_id=None):
    recipient = None
    reply_to = None
    if recipient_id:
        recipient = get_object_or_404(settings.AUTH_USER_MODEL, id=recipient_id)
    if reply_to_id:
        reply_to = get_object_or_404(Message, id=reply_to_id)

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            if reply_to:
                msg.recipient = reply_to.sender
                msg.reply_to = reply_to
            else:
                msg.recipient = recipient
            msg.save()
            return redirect('inbox')
    else:
        form = MessageForm()

    return render(request, 'send_message.html', {'form': form, 'recipient': recipient, 'reply_to': reply_to})

@login_required
def view_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    # تأكد المستخدم طرف في المحادثة
    if request.user != message.sender and request.user != message.recipient:
        return redirect('inbox')

    message.is_read = True
    message.save()

    replies = message.replies.all().order_by('created_at')
    form = MessageForm()  # form للرد
    return render(request, 'view_message.html', {'message': message, 'replies': replies, 'form': form})
