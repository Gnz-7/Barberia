from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Viernes, Sabado


@login_required
def inicio(request):
    
    return render(request,'inicio.html')

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
    
    if dia == 'viernes':
        mensaje = "Ya tenés un turno reservado para el viernes."
    elif dia == 'sabado':
        mensaje = "Ya tenés un turno reservado para el sábado."
    else:
        mensaje = "Ya tenés un turno reservado para ese día."
        
    return render(request, 'mensajes/advertencia.html', {'mensaje': mensaje})