from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, User
from django.contrib.auth import update_session_auth_hash
from . forms import EditarDatosForm, EditarContraseñaForm


# --------------------------------------------------------------------------------------------------


@login_required
def inicio(request):
    
    return render(request,'inicio.html')

# --------------------------------------------------------------------------------------------------


@login_required
def lunes(request):
    
    disponible = Lunes.objects.filter(cliente__isnull=True)
    
    return render(request, 'lunes/lunes.html', {'horarios': disponible})


@login_required
def reserva_lunes(request, turno_id):
    
    reserva = Lunes.objects.get(id=turno_id)

    if request.method == 'POST':
        
        turno_existente = Lunes.objects.filter(cliente=request.user).exists()

        if turno_existente:
            return redirect('advertencia', dia='lunes')
        else:
            reserva.cliente = request.user
            reserva.save()
            return redirect('exito')

    return render(request, 'lunes/reserva_lunes.html', {'turno': reserva})


# --------------------------------------------------------------------------------------------------


@login_required
def martes(request):
    
    disponible = Martes.objects.filter(cliente__isnull=True)
    
    return render(request, 'martes/martes.html', {'horarios': disponible})


@login_required
def reserva_martes(request, turno_id):
    
    reserva = Martes.objects.get(id=turno_id)

    if request.method == 'POST':
        
        turno_existente = Martes.objects.filter(cliente=request.user).exists()

        if turno_existente:
            return redirect('advertencia', dia='martes')
        else:
            reserva.cliente = request.user
            reserva.save()
            return redirect('exito')

    return render(request, 'martes/reserva_martes.html', {'turno': reserva})


# --------------------------------------------------------------------------------------------------


@login_required
def miercoles(request):
    
    disponible = Miercoles.objects.filter(cliente__isnull=True)
    
    return render(request, 'miercoles/miercoles.html', {'horarios': disponible})


@login_required
def reserva_miercoles(request, turno_id):
    
    reserva = Miercoles.objects.get(id=turno_id)

    if request.method == 'POST':
        
        turno_existente = Miercoles.objects.filter(cliente=request.user).exists()

        if turno_existente:
            return redirect('advertencia', dia='miercoles')
        else:
            reserva.cliente = request.user
            reserva.save()
            return redirect('exito')

    return render(request, 'miercoles/reserva_miercoles.html', {'turno': reserva})


# --------------------------------------------------------------------------------------------------

@login_required
def jueves(request):
    
    disponible = Jueves.objects.filter(cliente__isnull=True)
    
    return render(request, 'jueves/jueves.html', {'horarios': disponible})


@login_required
def reserva_jueves(request, turno_id):
    
    reserva = Jueves.objects.get(id=turno_id)

    if request.method == 'POST':
        
        turno_existente = Jueves.objects.filter(cliente=request.user).exists()

        if turno_existente:
            return redirect('advertencia', dia='jueves')
        else:
            reserva.cliente = request.user
            reserva.save()
            return redirect('exito')

    return render(request, 'jueves/reserva_jueves.html', {'turno': reserva})


# --------------------------------------------------------------------------------------------------

@login_required
def viernes(request):
    
    disponible = Viernes.objects.filter(cliente__isnull=True)
    
    return render(request, 'viernes/viernes.html', {'horarios': disponible})


@login_required
def reserva_viernes(request, turno_id):
    
    reserva = Viernes.objects.get(id=turno_id)

    if request.method == 'POST':
        
        turno_existente = Viernes.objects.filter(cliente=request.user).exists()

        if turno_existente:
            return redirect('advertencia', dia='viernes')
        else:
            reserva.cliente = request.user
            reserva.save()
            return redirect('exito')

    return render(request, 'viernes/reserva_viernes.html', {'turno': reserva})



# --------------------------------------------------------------------------------------------------

@login_required
def sabado(request):
    
    disponible = Sabado.objects.filter(cliente__isnull=True)
    
    return render(request, 'sabado/sabado.html', {'horarios': disponible})



@login_required
def reserva_sabado(request, turno_id):


    reserva = Sabado.objects.get(id=turno_id)

    if request.method == 'POST':
        
        turno_existente = Sabado.objects.filter(cliente=request.user).exists()

        if turno_existente:
            return redirect('advertencia', dia='sabado')
        else:
            reserva.cliente = request.user
            reserva.save()
            return redirect('exito')

    return render(request, 'sabado/reserva_sabado.html', {'turno': reserva})

# --------------------------------------------------------------------------------------------------

@login_required
def exito(request):
    
    return render(request,'mensajes/exito.html',{})


@login_required
def advertencia(request, dia):
    
    
    if dia == 'lunes':
        mensaje = "Ya tenés un turno reservado para el lunes."
    elif dia == 'martes':
        mensaje = "Ya tenés un turno reservado para el martes."
    elif dia == 'miercoles':
        mensaje = "Ya tenés un turno reservado para el miercoles."
    elif dia == 'jueves':
        mensaje = "Ya tenés un turno reservado para el jueves."
    elif dia == 'viernes':
        mensaje = "Ya tenés un turno reservado para el viernes."
    elif dia == 'sabado':
        mensaje = "Ya tenés un turno reservado para el sábado."
    else:
        mensaje = "Ya tenés un turno reservado para ese día."
        
    return render(request, 'mensajes/advertencia.html', {'mensaje': mensaje})

# --------------------------------------------------------------------------------------------------

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



@login_required
def cambiar_password(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)

    # Verificamos que el usuario que accede sea el mismo que está intentando cambiar su contraseña
    if request.user.id != usuario.id:
        return redirect('no_autorizado')  # O lanzá un Http404 o HttpResponseForbidden

    if request.method == 'POST':
        
        form = EditarContraseñaForm(request.POST)
        if form.is_valid():
            
            if not usuario.check_password(form.cleaned_data['password']):
                form.add_error('password', 'La contraseña actual es incorrecta.')
            else:
                usuario.set_password(form.cleaned_data['new_password'])
                usuario.save()
                update_session_auth_hash(request, usuario)  # 🔒 Esto mantiene la sesión activa
                return redirect('exito_datos')
    else:
        form = EditarContraseñaForm()

    return render(request, 'perfil/cambiar_password.html', {'form': form})


@login_required
def exito_datos(request):
    
    return render(request, 'perfil/exito_datos.html')