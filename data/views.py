from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from data.models import Data

class DataList(ListView):
    model = Data

class DataView(DetailView):
    model = Data

class DataCreate(CreateView):
    model = Data
    fields = ['name', 'pages']
    success_url = reverse_lazy('data_list')

class DataUpdate(UpdateView):
    model = Data
    fields = ['name', 'pages']
    success_url = reverse_lazy('data_list')

class DataDelete(DeleteView):
    model = Data
    success_url = reverse_lazy('data_list')

class DataForm(ModelForm):
    class Meta:
        model = Data
        fields = ['name', 'pages']

def data_list(request, template_name='data/data_list.html'):
    data = Data.objects.all()
    data = {}
    data['object_list'] = data
    return render(request, template_name, data)

def data_view(request, pk, template_name='data/data_detail.html'):
    data= get_object_or_404(Data, pk=pk)    
    return render(request, template_name, {'object':data})

def data_create(request, template_name='data/data_form.html'):
    form = DataForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('data_list')
    return render(request, template_name, {'form':form})

def data_update(request, pk, template_name='data/data_form.html'):
    data= get_object_or_404(Data, pk=pk)
    form = DataForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return redirect('data_list')
    return render(request, template_name, {'form':form})

def data_delete(request, pk, template_name='data/data_confirm_delete.html'):
    data= get_object_or_404(Book, pk=pk)    
    if request.method=='POST':
        book.delete()
        return redirect('data_list')
    return render(request, template_name, {'object':data})
