from .views import login, register, perfil, editar_perfil
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('perfil/', perfil, name='perfil'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('perfil/editar/', editar_perfil, name='editar_perfil')
]
