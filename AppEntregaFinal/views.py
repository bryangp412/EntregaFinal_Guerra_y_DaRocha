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
    
    prueba1= Pelicula(nombre='Pepe')
    prueba2= Pelicula(nombre='Pepa')
    prueba3= Pelicula(nombre='Pepq')
    
    render = template.render({'lista_objeto':[prueba1,prueba2,prueba3]})
    return HttpResponse(render)

def locales(request):
    template = loader.get_template('locales.html')

    prueba1= Locales(nombre='Pepe')
    prueba2= Locales(nombre='Pepa')
    prueba3= Locales(nombre='Pepq')
    
    render = template.render({'lista_objeto':[prueba1,prueba2,prueba3]})
    return HttpResponse(render)

def productos(request):
    template = loader.get_template('productos.html')
    prueba1= Locales(nombre='Pepe')
    prueba2= Locales(nombre='Pepa')
    prueba3= Locales(nombre='Pepq')
    
    render = template.render({'lista_objeto':[prueba1,prueba2,prueba3]})
    return HttpResponse(render)

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
def agregarlocal(request):
    return render(request, 'agregarlocal.html')
def agregarprodu(request):
    return render(request, 'agregarprodu.html')