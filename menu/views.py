from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from turnos.models import Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, User
from django.contrib.auth import update_session_auth_hash
from .forms import EditarDatosForm, EditarContraseñaForm


@login_required
def mis_turnos(request):
    # Buscar turnos de cada día
    turnos = {
        'lunes': Lunes.objects.filter(cliente=request.user).first(),
        'martes': Martes.objects.filter(cliente=request.user).first(),
        'miercoles': Miercoles.objects.filter(cliente=request.user).first(),
        'jueves': Jueves.objects.filter(cliente=request.user).first(),
        'viernes': Viernes.objects.filter(cliente=request.user).first(),
        'sabado': Sabado.objects.filter(cliente=request.user).first(),
    }

    mensajes = {}
    for dia, turno in turnos.items():
        if turno:
            mensajes[dia] = f"Reservaste para el {dia.capitalize()} a las {turno.horario}"
        else:
            mensajes[dia] = "No tenés turno reservado"

    return render(request, 'mis_turnos.html', {'mensajes': mensajes})

# --------------------------------------------------------------------------------------------------

@login_required
def ver_perfil(request, usuario_id):
    
    ver = User.objects.filter(id=usuario_id)
    
    return render(request, 'perfil/ver_perfil.html', {'ver': ver})

# --------------------------------------------------------------------------------------------------

@login_required
def editar(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)

    if request.method == 'POST':
        
        form = EditarDatosForm(request.POST)
        if form.is_valid():
            
            usuario.username = form.cleaned_data['nombre_usuario']
            usuario.email = form.cleaned_data['email']
            usuario.save()
            return redirect('ver_perfil', usuario_id=usuario.id)
    else:
        form = EditarDatosForm(initial={
            'nombre_usuario': usuario.username,
            'email': usuario.email
        })

    return render(request, 'perfil/editar.html', {'datos': usuario, 'form': form})

# --------------------------------------------------------------------------------------------------

@login_required
def cambiar_password(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)

    
    if request.user.id != usuario.id:
        return redirect('no_autorizado')  

    if request.method == 'POST':
        
        form = EditarContraseñaForm(request.POST)
        if form.is_valid():
            
            if not usuario.check_password(form.cleaned_data['password']):
                form.add_error('password', 'La contraseña actual es incorrecta.')
            else:
                usuario.set_password(form.cleaned_data['new_password'])
                usuario.save()
                update_session_auth_hash(request, usuario)  # Esto mantiene la sesión activa
                return redirect('ver_perfil', usuario_id=usuario.id)
    else:
        form = EditarContraseñaForm()

    return render(request, 'perfil/cambiar_password.html', {'form': form})
