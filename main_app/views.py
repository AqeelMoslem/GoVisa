# main_app/views.py
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .models import Visa, Message
from .forms import VisaForm, MessageForm, VisaStatusForm

# ------------------------------
# Home & About Views
# ------------------------------
def home(request):
    return render(request, 'home.html')

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

# ------------------------------
# Authentication Views
# ------------------------------
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('visa-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

# ------------------------------
# Visa Views
# ------------------------------
def visa_index(request):
    if request.user.is_staff:
        return redirect("admin-dashboard")
    visas = Visa.objects.filter(user=request.user).order_by("-travel_date")
    return render(request, "visas/index.html", {"visas": visas})

def visa_detail(request, visa_id):
    visa = Visa.objects.get(id=visa_id)
    return render(request, 'visas/detail.html', {'visa': visa})

@login_required
def create_visa(request):
    if request.user.is_staff:
        return redirect('admin-dashboard')
    form = VisaForm(request.POST or None)
    if form.is_valid():
        visa = form.save(commit=False)
        visa.user = request.user
        visa.save()
        return redirect('visa-index')
    return render(request, 'visas/create.html', {'form': form})

@login_required
def edit_visa(request, visa_id):
    visa = get_object_or_404(Visa, id=visa_id)
    if visa.user != request.user:
        return redirect('visa-index')
    form = VisaForm(request.POST or None, instance=visa)
    if form.is_valid():
        form.save()
        return redirect('visa-detail', visa_id=visa.id)
    return render(request, 'visas/edit.html', {'form': form, 'visa': visa})

class VisaCreate(LoginRequiredMixin, CreateView):
    model = Visa
    form_class = VisaForm
    success_url = reverse_lazy('visa-index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class VisaUpdate(UpdateView):
    model = Visa
    fields = ['passport_number', 'destination_country', 'travel_date']

class VisaDelete(DeleteView):
    model = Visa
    success_url = '/visas/'

# ------------------------------
# Message Views
# ------------------------------
@login_required
def inbox(request):
    messages_list = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'messages/inbox.html', {'messages': messages_list})

@login_required
def sent_messages(request):
    messages_list = Message.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'messages/sent.html', {'sent_messages': messages_list})

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

# ------------------------------
# Admin Views
# ------------------------------
@staff_member_required
def admin_dashboard(request):
    visas = Visa.objects.all().order_by("-travel_date")
    return render(request, "admin/dashboard.html", {"visas": visas})

@staff_member_required
def admin_messages(request):
    inbox_list = Message.objects.all().order_by("-timestamp")
    return render(request, "messages/detail.html", {"inbox": inbox_list})

@staff_member_required
def admin_reply_message(request, msg_id):
    msg = get_object_or_404(Message, id=msg_id)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.sender = request.user
            reply.receiver = msg.sender
            reply.save()
            return redirect("admin-messages")
    else:
        form = MessageForm()
    return render(request, "admin/reply.html", {"form": form, "msg": msg})

@staff_member_required
@require_POST
def update_visa_status(request, visa_id):
    visa = get_object_or_404(Visa, id=visa_id)
    new_status = request.POST.get("status")
    if new_status in dict(Visa.STATUS_CHOICES):
        visa.status = new_status
        visa.save()
    return redirect("admin-dashboard")

@staff_member_required
def admin_update_visa(request, visa_id):
    visa = get_object_or_404(Visa, id=visa_id)
    if request.method == "POST":
        upload_file = request.FILES.get("upload_file")
        status = request.POST.get("status")
        visa.status = status
        if upload_file:
            visa.document = upload_file

        admin_name = request.user.get_full_name() or request.user.username

        # تحديث الرسالة تلقائيًا للمستخدم مع اسم الادمن
        if status == "Approved":
            visa.user_message = f"Your visa has been approved by {admin_name}. Please wait for processing."
        elif status == "Completed" and upload_file:
            visa.user_message = f"Your document has been uploaded by {admin_name} successfully."
        elif status == "Rejected":
            visa.user_message = f"Your visa was rejected by {admin_name}. Please contact the admin."

        visa.save()
        return redirect("admin-dashboard")
    
    return render(request, "admin/dashboard.html", {"visas": [visa]})
