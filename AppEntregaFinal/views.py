from re import template
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def una_vista(request):
    return HttpResponse('<h1>Una vista</h1>')

def mi_template(request):
    template = loader.get_template('index.html')
    render = template.render({})
    return HttpResponse(render)