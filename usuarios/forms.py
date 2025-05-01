from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import InfoExtra

class FormularioRegistro(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class FurmularioEditPerfil(UserChangeForm):
    password = None  # El campo de la contraseña no es necesario
    email = forms.EmailField(required=False)  # Hacemos que el email sea opcional
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]

class FormularioInfoExtra(forms.ModelForm):
    avatar = forms.ImageField(required=False, label="Avatar")
    fecha_nacimiento = forms.DateField(
        label="Fecha de nacimiento", widget=forms.TextInput(attrs={'type': 'date'}), required=False
    )
    
    class Meta:
        model = InfoExtra
        fields = ["avatar", "fecha_nacimiento"]
