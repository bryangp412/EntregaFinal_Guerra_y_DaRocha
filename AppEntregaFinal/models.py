from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Pelicula(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    
class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    descripcion = RichTextField()
class Locales(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)