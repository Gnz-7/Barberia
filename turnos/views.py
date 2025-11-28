from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, User
from django.contrib import messages


# --------------------------------------------------------------------------------------------------


@login_required
def inicio(request):
    
    return render(request,'inicio.html')

# --------------------------------------------------------------------------------------------------

@login_required
def lunes(request):

    if request.method == 'POST':
        turno_id = request.POST.get('turno_id')

        if turno_id:
            try:
                turno = Lunes.objects.get(id=turno_id)
            except Lunes.DoesNotExist:
                mensaje = 'Turno no válido.'
            else:
                if Lunes.objects.filter(cliente=request.user).exists():
                    messages.error(request, 'Ya tenés un turno reservado.')
                else:
                    turno.cliente = request.user
                    turno.save()
                    messages.success(request, 'Turno reservado correctamente.')

        
        return redirect('lunes')

    disponible = Lunes.objects.all()
    return render(request, 'lunes.html', {'disponible': disponible})





# --------------------------------------------------------------------------------------------------


@login_required
def martes(request):

    if request.method == 'POST':
        turno_id = request.POST.get('turno_id')

        if turno_id:
            try:
                turno = Martes.objects.get(id=turno_id)
            except Martes.DoesNotExist:
                mensaje = 'Turno no válido.'
            else:
                if Martes.objects.filter(cliente=request.user).exists():
                    messages.error(request, 'Ya tenés un turno reservado.')
                else:
                    turno.cliente = request.user
                    turno.save()
                    messages.success(request, 'Turno reservado correctamente.')

        
        return redirect('martes')

    disponible = Martes.objects.all()
    return render(request, 'martes.html', {'disponible': disponible})


# --------------------------------------------------------------------------------------------------


@login_required
def miercoles(request):

    if request.method == 'POST':
        turno_id = request.POST.get('turno_id')

        if turno_id:
            try:
                turno = Miercoles.objects.get(id=turno_id)
            except Miercoles.DoesNotExist:
                mensaje = 'Turno no válido.'
            else:
                if Miercoles.objects.filter(cliente=request.user).exists():
                    messages.error(request, 'Ya tenés un turno reservado.')
                else:
                    turno.cliente = request.user
                    turno.save()
                    messages.success(request, 'Turno reservado correctamente.')

        
        return redirect('miercoles')

    disponible = Miercoles.objects.all()
    return render(request, 'miercoles.html', {'disponible': disponible})


# --------------------------------------------------------------------------------------------------

@login_required
def jueves(request):

    if request.method == 'POST':
        turno_id = request.POST.get('turno_id')

        if turno_id:
            try:
                turno = Jueves.objects.get(id=turno_id)
            except Jueves.DoesNotExist:
                mensaje = 'Turno no válido.'
            else:
                if Jueves.objects.filter(cliente=request.user).exists():
                    messages.error(request, 'Ya tenés un turno reservado.')
                else:
                    turno.cliente = request.user
                    turno.save()
                    messages.success(request, 'Turno reservado correctamente.')

        
        return redirect('jueves')

    disponible = Jueves.objects.all()
    return render(request, 'jueves.html', {'disponible': disponible})


# --------------------------------------------------------------------------------------------------

@login_required
def viernes(request):

    if request.method == 'POST':
        turno_id = request.POST.get('turno_id')

        if turno_id:
            try:
                turno = Viernes.objects.get(id=turno_id)
            except Viernes.DoesNotExist:
                mensaje = 'Turno no válido.'
            else:
                if Viernes.objects.filter(cliente=request.user).exists():
                    messages.error(request, 'Ya tenés un turno reservado.')
                else:
                    turno.cliente = request.user
                    turno.save()
                    messages.success(request, 'Turno reservado correctamente.')

        
        return redirect('viernes')

    disponible = Viernes.objects.all()
    return render(request, 'viernes.html', {'disponible': disponible})



# --------------------------------------------------------------------------------------------------

@login_required
def sabado(request):
    
    if request.method == 'POST':
        turno_id = request.POST.get('turno_id')

        if turno_id:
            try:
                turno = Sabado.objects.get(id=turno_id)
            except Sabado.DoesNotExist:
                mensaje = 'Turno no válido.'
            else:
                if Sabado.objects.filter(cliente=request.user).exists():
                    messages.error(request, 'Ya tenés un turno reservado.')
                else:
                    turno.cliente = request.user
                    turno.save()
                    messages.success(request, 'Turno reservado correctamente.')

        
        return redirect('sabado')

    disponible = Sabado.objects.all()
    return render(request, 'sabado.html', {'disponible': disponible})


# --------------------------------------------------------------------------------------------------

