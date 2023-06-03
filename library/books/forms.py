from django.forms import ModelForm 
from django import forms
from books.models import Carros


# Create the form class.
class CarrosForm(ModelForm):
    class Meta:
         model = Carros
         fields = ["modelo", "marca", "ano", "image"]
class Image(forms.Form):
     Image = forms.ImageField()
