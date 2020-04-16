from django.urls import path
from . import views

urlpatterns = [
    # path('asd/', views.ElectricityInformation.as_view(), name ='electricity_list'),


   # path('', views.electricity_list, name = 'electricity_list'),
    path('date/', views.HomeView.as_view(), name = 'home'),
    path(r'^date/$', views.HomeView.as_view(), name = 'electricity_list'),      # Maps the URL 
    
    # path('<int:date>/', views.electricity_list, name = 'electricity_list'),
   
 
]

           
    