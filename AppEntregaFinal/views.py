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
    lista_pelicula = Pelicula.objects.all()
    return render(request, 'cartelera.html',{"lista_pelicula": lista_pelicula})

def locales(request):
    lista_locales = Locales.objects.all()
    return render(request, 'locales.html',{"lista_locales": lista_locales})

def productos(request):
    lista_productos = Productos.objects.all()
    return render(request, 'productos.html',{"lista_productos": lista_productos})

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
def agregarlocal(request):
    if request.method == 'POST':
        form = LocalesForm (request.POST)
        
        if form.is_valid():
            data=form.cleaned_data
            locales = Locales(
                nombre=data.get('nombre'),
                direccion=data.get('direccion')
            )
            locales.save()
            lista_locales = Locales.objects.all()
            return render(request, 'locales.html',{"lista_locales": lista_locales})
        else:
            return render(request, 'agregarlocal.html', {'form':form})
    
    form_locales =PeliculaForm()
    return render(request, 'agregarlocal.html',{"form":form_locales})
def agregarprodu(request):
    if request.method == 'POST':
        form = ProductoForm (request.POST)
        
        if form.is_valid():
            data=form.cleaned_data
            producto = Productos(
                nombre=data.get('nombre'),
                precio=data.get('precio')
            )
            producto.save()
            lista_productos = Productos.objects.all()
            return render(request, 'productos.html',{"lista_productos": lista_productos})
        else:
            return render(request, 'agregarprodu.html', {'form':form})
    
    form_producto =PeliculaForm()
    return render(request, 'agregarprodu.html',{"form":form_producto})

