
from re import template
from tkinter.tix import Form
from django import forms

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from AppEntregaFinal.forms import BuscaLocales, BuscaPelicula, BuscaProductos, LocalesForm, PeliculaForm, ProductoForm
from django.contrib.auth.decorators import login_required

from AppEntregaFinal.models import Pelicula, Locales, Productos
# Create your views here.

def index(request):
    return render(request, 'index.html')

def cartelera(request):
    
    nombre_de_busqueda = request.GET.get('nombre')
    
    if nombre_de_busqueda:
        lista_pelicula = Pelicula.objects.filter(nombre__icontains=nombre_de_busqueda)
    else:
        lista_pelicula = Pelicula.objects.all()
    
    form=BuscaPelicula()    
    return render(request, 'cartelera.html',{"lista_pelicula": lista_pelicula, "form": form})

def locales(request):
    
    nombre_de_busqueda = request.GET.get('nombre')
    
    if nombre_de_busqueda:
        lista_locales = Locales.objects.filter(nombre__icontains=nombre_de_busqueda)
    else: 
        lista_locales = Locales.objects.all()
        
    form=BuscaLocales()
    return render(request, 'locales.html',{"lista_locales": lista_locales, "form": form})

def productos(request):
    
    nombre_de_busqueda = request.GET.get('nombre')
    
    if nombre_de_busqueda:
        lista_productos = Productos.objects.filter(nombre__icontains=nombre_de_busqueda)
    else: 
        lista_productos = Productos.objects.all()
        
    form=BuscaProductos()
    return render(request, 'productos.html',{"lista_productos": lista_productos, "form": form})

def privacidad(request):
    return render(request, 'privacidad.html')

def terminos(request):
    return render(request, 'terminos.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')

@login_required
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
            
            return redirect('cartelera')
        else:
            return render(request, 'agregarpeli.html', {'form':form})
    
    form_pelicula =PeliculaForm()
    return render(request, 'agregarpeli.html',{"form":form_pelicula})

@login_required
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
            return redirect('locales')
        else:
            return render(request, 'agregarlocal.html', {'form':form})
    
    form_locales =LocalesForm()
    return render(request, 'agregarlocal.html',{"form":form_locales})


@login_required
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
            return redirect('productos')
        else:
            return render(request, 'agregarprodu.html', {'form':form})
    
    form_producto =ProductoForm()
    return render(request, 'agregarprodu.html',{"form":form_producto})

@login_required
def cartelera_log(request):
    nombre_de_busqueda = request.GET.get('nombre')
    
    if nombre_de_busqueda:
        lista_pelicula = Pelicula.objects.filter(nombre__icontains=nombre_de_busqueda)
    else:
        lista_pelicula = Pelicula.objects.all()
    
    form=BuscaPelicula()    
    return render(request, 'cartelera_logeado.html',{"lista_pelicula": lista_pelicula, "form": form})


@login_required
def editar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    
    if request.method == 'POST':
        form = PeliculaForm (request.POST)
        if form.is_valid():
            pelicula.nombre = form.cleaned_data.get('nombre')
            pelicula.categoria = form.cleaned_data.get('categoria')
            pelicula.save()
            
            return redirect('cartelera_log')
        else:
            return render(request, 'editarpeli.html', {'form':form, 'pelicula':pelicula})
        
    form_pelicula =PeliculaForm(initial={'nombre':pelicula.nombre, 'categoria':pelicula.categoria})
    return render(request, 'editarpeli.html',{"form":form_pelicula, 'pelicula':pelicula})

@login_required
def eliminar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()
    return redirect('cartelera_log')

@login_required
def locales_log(request):
    nombre_de_busqueda = request.GET.get('nombre')
    
    if nombre_de_busqueda:
        lista_locales = Locales.objects.filter(nombre__icontains=nombre_de_busqueda)
    else: 
        lista_locales = Locales.objects.all()
        
    form=BuscaLocales()
    return render(request, 'locales_logeado.html',{"lista_locales": lista_locales, "form": form})

@login_required
def editar_local(request, id):
    local = Locales.objects.get(id=id)
    
    if request.method == 'POST':
        form = LocalesForm (request.POST)
        if form.is_valid():
            local.nombre = form.cleaned_data.get('nombre')
            local.direccion = form.cleaned_data.get('direccion')
            local.save()
            
            return redirect('locales_log')
        else:
            return render(request, 'editarlocal.html', {'form':form, 'local':local})
        
    form_local =LocalesForm(initial={'nombre':local.nombre, 'direccion':local.direccion})
    return render(request, 'editarlocal.html',{"form":form_local, 'local':local})


@login_required
def eliminar_local(request, id):
    local = Locales.objects.get(id=id)
    local.delete()
    return redirect('locales_log')

@login_required
def productos_log(request):
    nombre_de_busqueda = request.GET.get('nombre')
    
    if nombre_de_busqueda:
        lista_productos = Productos.objects.filter(nombre__icontains=nombre_de_busqueda)
    else: 
        lista_productos = Productos.objects.all()
        
    form=BuscaProductos()
    return render(request, 'productos_logeado.html',{"lista_productos": lista_productos, "form": form})


@login_required
def editar_producto(request, id):
    producto = Productos.objects.get(id=id)
    
    if request.method == 'POST':
        form = ProductoForm (request.POST)
        if form.is_valid():
            producto.nombre = form.cleaned_data.get('nombre')
            producto.precio = form.cleaned_data.get('precio')
            producto.save()
            
            return redirect('productos_log')
        else:
            return render(request, 'editarprod.html', {'form':form, 'producto':producto})
        
    form_producto =ProductoForm(initial={'nombre':producto.nombre, 'precio':producto.precio})
    return render(request, 'editarprodu.html',{"form":form_producto, 'producto':producto})

@login_required
def eliminar_producto(request, id):
    producto = Productos.objects.get(id=id)
    producto.delete()
    return redirect('productos_log')

@login_required
def mostrar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    return render(request, 'mostrarpeli.html', {'pelicula':pelicula})

@login_required
def mostrar_producto(request, id):
    producto = Productos.objects.get(id=id)
    return render(request, 'mostrarprodu.html', {'producto':producto})

@login_required
def mostrar_local(request, id):
    local = Locales.objects.get(id=id)
    return render(request, 'mostrarlocal.html', {'local':local})
    