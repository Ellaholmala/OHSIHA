from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render, reverse
from django.urls import reverse_lazy

from django.shortcuts import render, redirect, get_object_or_404 # Tarviiko?
from django.forms import ModelForm
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Sum

from electricity.forms import DateForm
import sys, datetime
# Create your views here.
from electricity.models import ElectricityData  # Imports created Electricity model

class ElectricityInformation(ListView):  # Variable 198
    model = ElectricityData

class HomeView(TemplateView):
    template_name = 'electricity/date.html'

    def get(self, request):
        date = request.GET.get('date', '')
        if date != "":
            # Filters data by type of data
            splitdata = date.split(".")
            #datetime.date(int(splitdata[2]), int(splitdata[1]), int(splitdata[0]))
            selected_date = ElectricityData.objects.all().filter(start_time__contains=datetime.date(int(splitdata[2]), int(splitdata[1]), int(splitdata[0])))
            # print(ElectricityData.objects.first().start_time, file=sys.stdout)
            # print(f"{splitdata[2]}-{splitdata[1]}-{splitdata[0]}", file=sys.stdout)
            # print(selected_date.count(), file=sys.stdout)
            # print(ElectricityData.objects.all().count(), file=sys.stdout)
            # print(datetime.date(int(splitdata[2]), int(splitdata[1]), int(splitdata[0])), file=sys.stdout)
            data = {}
            surplus = selected_date.filter(variable_id=198)         #.objects?
            production = selected_date.filter(variable_id=192)      #.objects?
            consumption = selected_date.filter(variable_id=193)     #.objects?

            night = 0
            day = 0
            evening = 0

            date_prefix = f"{splitdata[2]}-{splitdata[1]}-{splitdata[0]} "
            
            # print(f"{date_prefix}00:00", file=sys.stdout)
            surplus_night = surplus.filter(start_time__range=[f"{date_prefix}00:00", f"{date_prefix}08:00"]).aggregate(Sum('value'))#.aggregate(Sum('value')).get('value__sum', 0.00)
            production_night = production.filter(start_time__range=[f"{date_prefix}00:00", f"{date_prefix}08:00"]).aggregate(Sum('value'))
            consumption_night = consumption.filter(start_time__range=[f"{date_prefix}00:00", f"{date_prefix}08:00"]).aggregate(Sum('value'))
            
            surplus_day = surplus.filter(start_time__range=[f"{date_prefix}08:01", f"{date_prefix}16:00"]).aggregate(Sum('value'))
            production_day = production.filter(start_time__range=[f"{date_prefix}08:01", f"{date_prefix}16:00"]).aggregate(Sum('value'))
            consumption_day = consumption.filter(start_time__range=[f"{date_prefix}08:01", f"{date_prefix}16:00"]).aggregate(Sum('value'))

            surplus_evening = surplus.filter(start_time__range=[f"{date_prefix}16:01", f"{date_prefix}23:59"]).aggregate(Sum('value'))
            production_evening = production.filter(start_time__range=[f"{date_prefix}16:01", f"{date_prefix}23:59"]).aggregate(Sum('value'))
            consumption_evening = consumption.filter(start_time__range=[f"{date_prefix}16:01", f"{date_prefix}23:59"]).aggregate(Sum('value'))

            data["surplus_night"] = surplus_night
            data["surplus"] = [surplus_night["value__sum"], surplus_day["value__sum"], surplus_evening["value__sum"]]
            data["consumption"] = [consumption_night["value__sum"], consumption_day["value__sum"], consumption_evening["value__sum"]]
            data["production"] = [production_night["value__sum"], production_day["value__sum"], production_evening["value__sum"]]
            return render(request, "electricity/electricitydata_list.html", data)
        form = DateForm()
        return render(request, self.template_name,{'form':form})
        
    def post(self, request):
        date = request.POST.get('date')
        return redirect(reverse('electricity_list') + f'?date={date}')
      


