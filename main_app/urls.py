from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('visas/', views.visa_index, name='visa-index'),
    path('visas/<int:visa_id>/', views.visa_detail, name='visa-detail'),
    path('visas/create/', views.VisaCreate.as_view(), name='visa-create'),
    path('visas/<int:pk>/update/', views.VisaUpdate.as_view(), name='visa-update'),
    path('visas/<int:pk>/delete/', views.VisaDelete.as_view(), name='visa-delete'),

    path('inbox/', views.inbox, name='inbox'),
    path('message/<int:message_id>/', views.message_detail, name='message-detail'),
    path('message/new/', views.new_message, name='new-message'),
   
    
    path('accounts/signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path("dashboard/", views.admin_dashboard, name="admin-dashboard"),
    path("messages/", views.admin_messages, name="admin-messages"),
    path("messages/<int:msg_id>/reply/", views.admin_reply_message, name="admin-reply-message"),
    path("visa/<int:visa_id>/update/", views.admin_update_visa, name="admin-update-visa"),

]