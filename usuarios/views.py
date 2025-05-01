from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login as django_login
from usuarios.forms import FormularioRegistro, FurmularioEditPerfil, FormularioInfoExtra
from django.contrib.auth.decorators import login_required
from usuarios.models import InfoExtra

# Create your views here.
def login(request):
    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            
            usuario = formulario.get_user()
            
            django_login(request, usuario)
            
            InfoExtra.objects.get_or_create(user=usuario)

            return redirect("Main:index")
    else:
        formulario = AuthenticationForm()
    
    return render(request, "usuarios/login.html", context={"formulario": formulario})

def register(request):
    if request.method == "POST":
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            
            formulario.save()

            return redirect("usuarios:login")
    else:
        formulario = FormularioRegistro()
    
    return render(request, "usuarios/register.html", context={"formulario": formulario})

@login_required
def editar_perfil(request):
    try:
        infoextra = request.user.infoextra
    except InfoExtra.DoesNotExist:
        
        infoextra = InfoExtra.objects.create(user=request.user)

    if request.method == "POST":
        
        formulario = FurmularioEditPerfil(request.POST, request.FILES, instance=request.user)
        
        formulario_infoextra = FormularioInfoExtra(request.POST, request.FILES, instance=infoextra)
        
        if formulario.is_valid() and formulario_infoextra.is_valid():
            formulario.save()  
            formulario_infoextra.save()  

            
            return redirect("usuarios:perfil")
    else:
        
        formulario = FurmularioEditPerfil(instance=request.user)
        formulario_infoextra = FormularioInfoExtra(instance=infoextra)

    return render(request, "usuarios/editar_perfil.html", context={"formulario": formulario, "formulario_infoextra": formulario_infoextra})


def perfil(request):
    return render(request, "usuarios/perfil.html", context={"usuario": request.user})
