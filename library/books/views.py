from django.shortcuts import render
from books.forms import CarrosForm
# Create your views here.

def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)