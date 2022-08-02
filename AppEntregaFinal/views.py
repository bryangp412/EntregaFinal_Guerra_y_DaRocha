from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from AppEntregaFinal.models import Pelicula, Locales,Productos
# Create your views here.

def index(request):
    return render(request, 'index.html')

def cartelera(request):
    template = loader.get_template('cartelera.html')
    
    prueba1= Prueba(nombre='Pepe')
    prueba2= Prueba(nombre='Pepa')
    prueba3= Prueba(nombre='Pepq')
    
    render = template.render({'lista_objeto':[prueba1,prueba2,prueba3]})
    return HttpResponse(render)

def locales(request):
    return render(request, 'locales.html')

def productos(request):
    return render(request, 'productos.html')

def privacidad(request):
    return render(request, 'privacidad.html')

def terminos(request):
    return render(request, 'terminos.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')
def agregarpeli(request):
    return render(request, 'agregarpeli.html')