from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Usuario', max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
        help_texts = { key: '' for key in fields }
        
class MyUserEditForm(forms.Form):
    
    first_name = forms.CharField(label='Nombre', max_length=30, required=False)
    email = forms.EmailField(required=False)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirme contraseña', widget=forms.PasswordInput, required=False)
    avatar = forms.ImageField(label='Avatar', required=False)
    