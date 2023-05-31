from django.db import models
from uuid import uuid4
# Create your models here.

class Books(models.Model):
    id_car = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    car = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    titles = models.CharField(max_length=50)
    wins = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)

def upload_image_car(instace,fillename):
    return f"{instace.id_car}-{fillename}"

class Carros(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    image = models.ImageField(upload_to=upload_image_car, blank=True, null=True)