from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError

# Create your views here.

def bienvenido(request):
    return render(request, 'bienvenido.html')

def Registro(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('categorias')
            except IntegrityError:
                return render(request, 'registro.html', {'form': UserCreationForm, 'error': 'Error, el usuario ya existe.'})
        return render(request, 'registro.html', {'form': UserCreationForm, 'error': 'Error, las contraseñas no coinciden.'})
    else:
        return render(request, 'registro.html', {'form': UserCreationForm})

def IniciarSesion(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, 'iniciar.html', {'form': AuthenticationForm, 'error': 'Error, el usuario no existe.'})
        else:
            login(request,user)
            return redirect('categorias')
    else:
        return render(request, 'iniciar.html', {'form': AuthenticationForm})

def CerrarSesion(request):
    logout(request)
    return redirect('iniciar_sesion')