from django.urls import path
from .views import agregarlocal, agregarpeli, agregarprodu, contacto, index, cartelera, locales, nosotros, productos, privacidad, terminos

urlpatterns = [
    path("", index, name="index"),
    path('cartelera', cartelera, name="cartelera"),
    path('locales', locales),
    path('productos', productos),
    path("principal", index),
    path("privacidad", privacidad, name="privacidad"),
    path("terminos", terminos, name="terminos"),
    path("nosotros", nosotros, name="nosotros"),
    path("contacto", contacto, name="contacto"),
    path("agregarpeli", agregarpeli, name="agregarpeli"),
    path("agregarprodu", agregarprodu, name="agregarprodu"),
    path("agregarlocal", agregarlocal, name="agregarlocal"),
    
    
    
]
