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
    # path('inbox/', inbox, name='inbox'),
    # path('send/<int:recipient_id>/', send_message, name='send_message'),
    # path('reply/<int:reply_to_id>/', send_message, name='reply_message'),
    # path('message/<int:message_id>/', view_message, name='view_message'),
    # path('visas/<int:horse_id>/add_feeding/', views.add_feeding, name='add-feeding'),
    # path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
    # path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
    # path('toys/', views.ToyList.as_view(), name='toy-index'),
    # path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
    # path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
    # path('visas/<int:horse_id>/associate-toy/<int:toy_id>/', views.associate_toy, name='associate-toy'),
    # path('visas/<int:horse_id>/remove-toy/<int:toy_id>/', views.remove_toy, name='remove-toy'),
    # path('accounts/signup/', views.signup, name='signup'),
    # path('logout/', views.logout_view, name='logout'),


   
]