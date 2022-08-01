from django.urls import path
from .views import una_vista,mi_template

urlpatterns = [
    path('', una_vista),
    path('mi_template', mi_template)
]
