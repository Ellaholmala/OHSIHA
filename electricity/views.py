from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.urls import reverse_lazy

from django.shortcuts import render, redirect, get_object_or_404 # Tarviiko?
from django.forms import ModelForm
# Create your views here.
from electricity.models import ElectricityData  # Imports created Electricity model

class ElectricitySurplus(ListView):  # Variable 198
    model = ElectricityData
    
# class ElectricityProduction(DetailView):  # Variable 192
#     model = ElectricityData

# class ElectricityConsumption(DetailView): # Variable 193
#     model = ElectricityData
#def HomePageView(request):

 #   return render(request, 'electricity.html',{})

def surplus_list(request, template_name='electricity/electricity.html'):        # Lists the data
   
    data =  ElectricityData.objects.all()
    data = {}
    data['object_list'] = data

    return render(request, template_name, data)

# def production_list(request, template_name='electricity/electricity.html'):
#     # KUTSU DATA_READERIA
#     data = ElectricityData.objects.all()
#     data = {}
#     data['object_list'] = data
#     return render(request, template_name, data)

# def consumption_list(request, template_name='electricity/electricity.html'):
#     # KUTSU DATA_READERIA
#     data = ElectricityData.objects.all()
#     data = {}
#     data['object_list'] = data
#     return render(request, template_name, data)