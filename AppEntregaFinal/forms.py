from django import forms


class LocalesForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=40)

class PeliculaForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    categoria = forms.CharField(max_length=40)

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    precio = forms.FloatField()
    
class BuscaPelicula(forms.Form):
    nombre = forms.CharField(max_length=40, required=False)
    
class BuscaLocales(forms.Form):
    nombre = forms.CharField(max_length=40, required=False)

class BuscaProductos(forms.Form):
    nombre = forms.CharField(max_length=40, required=False)