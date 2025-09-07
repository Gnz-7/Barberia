from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Lunes, Martes, Miercoles, Jueves, Viernes, Sabado


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