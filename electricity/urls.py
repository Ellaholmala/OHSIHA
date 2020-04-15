from django.urls import path
from . import views

urlpatterns = [
    path('', views.ElectricitySurplus.as_view(), name ='surplus_list'),
    # path('', views.ElectricityProduction.as_view(), name = 'production_list'),
    # path('', views.ElectricityConsumption.as_view(), name = 'consumption_list'),

    path('', views.surplus_list, name = 'surplus_list'),
    # path('', views.production_list, name = 'production_list'),
    # path('', views.consumption_list, name = 'consumption_list')
]

           
    