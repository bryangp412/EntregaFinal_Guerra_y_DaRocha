from re import template
from django import forms

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppEntregaFinal.forms import LocalesForm, PeliculaForm, ProductoForm

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
    if request.method == 'POST':
        form = PeliculaForm (request.POST)
        
        if form.is_valid():
            data=form.cleaned_data
            pelicula = Pelicula(
                nombre=data.get('nombre'),
                categoria=data.get('categoria')
            )
            pelicula.save()
            lista_pelicula = Pelicula.objects.all()
            return render(request, 'cartelera.html',{"lista_pelicula": lista_pelicula})
        else:
            return render(request, 'agregarpeli.html', {'form':form})
    
    form_pelicula =PeliculaForm()
    return render(request, 'agregarpeli.html',{"form":form_pelicula})
def lista_pelicula(request):
    template = loader.get_template('cartelera.html')
    lista_pelicula = Pelicula.objects.all()
    render = template.render({'lista_pelicula': lista_pelicula})
    return HttpResponse(render)
def agregarlocal(request):
    return 0
def agregarprodu(request):
    if request.method == "POST":
        formularioProducto = ProductoForm(request.POST)
        if formularioProducto.is_valid():
            informacion = formularioProducto.cleaned_data
            producto = Productos()
            producto.nombre = informacion['nombre']
            producto.precio = informacion['precio']
            producto.save()
    else:
        formularioProducto = ProductoForm()   
    return render(request, 'agregarprodu.html')

