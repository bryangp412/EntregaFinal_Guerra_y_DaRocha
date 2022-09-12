from django.urls import path
from django.contrib import admin
from .views import agregarlocal, agregarpeli, agregarprodu, contacto, index, cartelera, locales, mostrar_local, mostrar_pelicula, mostrar_producto, nosotros, productos, privacidad, terminos, cartelera_log, locales_log, productos_log, editar_pelicula, eliminar_pelicula, editar_local, eliminar_local, editar_producto, eliminar_producto

urlpatterns = [
    path("", index, name="index"),
    path('cartelera/', cartelera, name="cartelera"),
    path('locales/', locales, name="locales"),
    path('productos/', productos, name="productos"),
    path("principal/", index, name='index'),
    path("privacidad/", privacidad, name="privacidad"),
    path("terminos/", terminos, name="terminos"),
    path("about/", nosotros, name="nosotros"),
    path("contacto/", contacto, name="contacto"),
    path("agregarpeli/", agregarpeli, name="agregarpeli"),
    path("agregarprodu/", agregarprodu, name="agregarprodu"),
    path("agregarlocal/", agregarlocal, name="agregarlocal"),
    path("carteleralog/", cartelera_log, name="cartelera_log"),
    path("editarpeli/<int:id>/", editar_pelicula, name="editar_pelicula"),
    path("eliminarpeli/<int:id>/", eliminar_pelicula, name="eliminar_pelicula"),
    path("localeslog/", locales_log, name="locales_log"),
    path("editarlocal/<int:id>/", editar_local, name="editar_local"),
    path("eliminarlocal/<int:id>/", eliminar_local, name="eliminar_local"),
    path("productoslog/", productos_log, name="productos_log"),
    path("editarprodu/<int:id>/", editar_producto, name="editar_producto"),
    path("eliminarprodu/<int:id>/", eliminar_producto, name="eliminar_producto"),
    path("mostrarprodu/<int:id>/", mostrar_producto, name="mostrar_producto"),
    path("mostrarlocal/<int:id>/", mostrar_local, name="mostrar_local"),
    path("mostrarpeli/<int:id>/", mostrar_pelicula, name="mostrar_pelicula"),
    
]
