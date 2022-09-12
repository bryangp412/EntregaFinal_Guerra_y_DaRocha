from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from accounts.models import MasDatos
from .form import MyUserCreationForm, MyUserEditForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username,password=password)
            
            if user is not None:
                django_login(request, user)
                return redirect('index')
            else:
                return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})
                
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else: 
            return render(request, 'register.html', {'form': form})
            
    form = MyUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'perfil.html')

@login_required
def editar_perfil(request):
    user = request.user
    mas_datos, _ = MasDatos.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        form = MyUserEditForm(request.POST, request.FILES)
        if form.is_valid():
            data =  form.cleaned_data
            if data.get('first_name'):
                user.first_name = data.get('first_name')
            user.email = data.get('email')
            mas_datos.avatar = data.get('avatar') if data.get('avatar') else mas_datos.avatar
            
            if data.get('password1') and data.get('password1') == data.get('password2'):
                user.set_password(data.get('password1'))
            mas_datos.save()
            user.save()
            return redirect('perfil')
        else:
            return render(request, 'editarperfil.html', {'form':form})
        
    form = MyUserEditForm(
        initial={
            'first_name': user.first_name,
            'email': user.email,
            'avatar': mas_datos.avatar
        }
    )
    return render(request, 'editarperfil.html', {'form':form})

