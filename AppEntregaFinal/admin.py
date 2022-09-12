from django.contrib import admin

from .models import Locales, Pelicula, Productos

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Productos)
admin.site.register(Locales)
