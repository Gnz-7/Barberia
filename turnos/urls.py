from django.urls import path
from . import views



urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    
    path('lunes/', views.lunes, name='lunes'),
    path('reserva_lunes/<int:turno_id>/', views.reserva_lunes, name='reserva_lunes'),
    
    path('martes/', views.martes, name='martes'),
    path('reserva_martes/<int:turno_id>/', views.reserva_martes, name='reserva_martes'),
    
    path('miercoles/', views.miercoles, name='miercoles'),
    path('reserva_miercoles/<int:turno_id>/', views.reserva_miercoles, name='reserva_miercoles'),
    
    path('jueves/', views.jueves, name='jueves'),
    path('reserva_jueves/<int:turno_id>/', views.reserva_jueves, name='reserva_jueves'),
    
    path('viernes/', views.viernes, name='viernes'),
    path('reserva_viernes/<int:turno_id>/', views.reserva_viernes, name='reserva_viernes'),
    
    path('sabado/', views.sabado, name='sabado'),
    path('reserva_sabado/<int:turno_id>/', views.reserva_sabado, name='reserva_sabado'),
    
    path('exito/', views.exito, name='exito'),
    path('advertencia/<str:dia>/', views.advertencia,name='advertencia'),
    
    path('mis_turnos/', views.mis_turnos, name='mis_turnos'),
    
    path('ver_perfil/<int:usuario_id>/', views.ver_perfil, name='ver_perfil'),
    path('editar/<int:usuario_id>/', views.editar, name='editar'),
    path('cambiar_password/<int:usuario_id>/', views.cambiar_password, name='cambiar_password' ),
    path('exito_datos/', views.exito_datos, name='exito_datos')

    
    
]
