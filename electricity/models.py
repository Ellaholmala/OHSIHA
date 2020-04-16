from django.db import models
from django.urls import reverse
from django import forms
# Create your models here.

class ElectricityData(models.Model): 
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    variable_id = models.IntegerField()
    value = models.FloatField()

    def __str__(self):
        return str(self.variable_id)
        

class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])