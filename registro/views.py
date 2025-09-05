# Create your views here.
from django.shortcuts import render,redirect
from .forms import RegistroForm
from django.contrib.auth import login, logout

# Create your views here.

def register(request):
    
    if request.method == 'POST':
        formulario = RegistroForm(request.POST)
        
        if formulario.is_valid():
            usuario = formulario.save()
            login(request,usuario)
            return redirect('inicio')
    
    else:
        formulario = RegistroForm()
    
    
    return render(request, 'register.html', {'datos': formulario})


def salir(request):
    logout(request)
    return redirect('index')