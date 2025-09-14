from django.urls import path
from . import views # Import views to connect routes to view functions


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('visas/', views.visa_index, name='visa-index'),
    path('visas/<int:horse_id>/', views.visa_detail, name='visa-detail'),
    path('visas/create/', views.VisaCreate.as_view(), name='visa-create'),
    path('visas/<int:pk>/update/', views.HorseUpdate.as_view(), name='horse-update'),
    path('visas/<int:pk>/delete/', views.HorseDelete.as_view(), name='horse-delete'),
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