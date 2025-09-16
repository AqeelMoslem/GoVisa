from django.urls import path
from . import views # Import views to connect routes to view functions
# from .views import inbox, send_message, view_message

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('visas/', views.visa_index, name='visa-index'),
    path('visas/<int:visa_id>/', views.visa_detail, name='visa-detail'),
    path('visas/create/', views.VisaCreate.as_view(), name='visa-create'),
    path('visas/<int:pk>/update/', views.VisaUpdate.as_view(), name='visa-update'),
    path('visas/<int:pk>/delete/', views.VisaDelete.as_view(), name='visa-delete'),

    path("inbox/", views.inbox, name="inbox"),
    path("sent/", views.sent_messages, name="sent-messages"),
    path("message/<int:message_id>/", views.message_detail, name="message-detail"),
    path("message/new/", views.new_message, name="new-message"),

   
    
    path('accounts/signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path("admin/dashboard/", views.admin_dashboard, name="admin-dashboard"),
    path("admin/visa/<int:visa_id>/update-status/", views.update_visa_status, name="update-visa-status"),
    path("admin/messages/", views.admin_messages, name="admin-messages"),
    path("admin/messages/<int:msg_id>/reply/", views.admin_reply_message, name="admin-reply-message"),
    



   
]