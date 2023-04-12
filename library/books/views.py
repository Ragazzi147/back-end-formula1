from django.shortcuts import render
from books.forms import CarrosForms
# Create your views here.

def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = CarrosForms()
    return render(request, 'form.html', data)