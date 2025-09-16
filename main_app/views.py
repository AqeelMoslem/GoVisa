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


# def visa_index(request):
#     visas = Visa.objects.filter(user=request.user)
#     return render(request, 'visas/index.html', { 'visas': visas })
# def visa_index(request):
#     if request.user.is_staff:  
#         visas = Visa.objects.all().order_by("-travel_date")  # الأدمن يشوف الكل
#     else:
#         visas = Visa.objects.filter(user=request.user).order_by("-travel_date")  # اليوزر يشوف طلباته فقط
#     return render(request, 'visas/index.html', {'visas': visas})

def visa_index(request):
    if request.user.is_staff:
        return redirect("admin-dashboard")
    visas = Visa.objects.filter(user=request.user).order_by("-travel_date")
    return render(request, "visas/index.html", {"visas": visas})

# views.py

def visa_detail(request, visa_id):
    visa = Visa.objects.get(id=visa_id)
    return render(request, 'visas/detail.html', {'visa': visa})

# main-app/views.py

class VisaCreate(LoginRequiredMixin,CreateView):
    model = Visa
    form_class = VisaForm      
    success_url = reverse_lazy('visa-index') 
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)

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

class Home(LoginView):
    template_name = 'home.html'


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('visa-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home') 
    
# main_app/views.py
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_dashboard(request):
    visas = Visa.objects.all().order_by("-travel_date")
    return render(request, "admin/dashboard.html", {"visas": visas})

@staff_member_required
def admin_messages(request):
    inbox = Message.objects.all().order_by("-timestamp")
    return render(request, "messages/detail.html", {"inbox": inbox})

@staff_member_required
def admin_reply_message(request, msg_id):
    msg = get_object_or_404(Message, id=msg_id)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.sender = request.user
            reply.receiver = msg.sender   # يرد على صاحب الرسالة
            reply.save()
            return redirect("admin-messages")
    else:
        form = MessageForm()
    return render(request, "admin/reply.html", {"form": form, "msg": msg})

from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect

@staff_member_required
@require_POST
def update_visa_status(request, visa_id):
    visa = get_object_or_404(Visa, id=visa_id)
    new_status = request.POST.get("status")
    if new_status in dict(Visa.STATUS_CHOICES):
        visa.status = new_status
        visa.save()
    return redirect("admin-dashboard")


from django.contrib import messages
from .forms import VisaStatusForm

@staff_member_required
def admin_update_visa(request, visa_id):
    visa = get_object_or_404(Visa, id=visa_id)
    
    if request.method == "POST":
        upload_file = request.FILES.get("upload_file")
        status = request.POST.get("status")

        visa.status = status
        if upload_file:
            visa.document = upload_file  # يخزن الملف في الحقل
        visa.save()

        # Alerts
        from django.contrib import messages
        if status == "Approved":
            messages.info(request, "تمت الموافقة، المعاملة ستأخذ بعض الوقت.")
        elif status == "Completed" and upload_file:
            messages.success(request, "تم رفع الملف بنجاح.")

        return redirect("admin-dashboard")

    return render(request, "admin/dashboard.html", {"visas": [visa]})

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect

# فحص لو المستخدم Staff
def is_staff(user):
    return user.is_staff


@login_required
def create_visa(request):
    if request.user.is_staff:
        return redirect('admin-dashboard')  # الأدمن ما يسوي Create هنا
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
    
    # فقط صاحب الفيزا يقدر يعدل
    if visa.user != request.user:
        return redirect('visa-index')
    
    form = VisaForm(request.POST or None, instance=visa)
    if form.is_valid():
        form.save()
        return redirect('visa-detail', visa_id=visa.id)
    return render(request, 'visas/edit.html', {'form': form, 'visa': visa})
