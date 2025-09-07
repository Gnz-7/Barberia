from django.urls import path
from . import views



urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('viernes/', views.viernes, name='viernes'),
    path('reserva_viernes/<int:turno_id>/', views.reserva_viernes, name='reserva_viernes'),
    path('sabado/', views.sabado, name='sabado'),
    path('reserva_sabado/<int:turno_id>/', views.reserva_sabado, name='reserva_sabado'),
    path('exito/', views.exito, name='exito'),
    path('advertencia/<str:dia>/', views.advertencia,name='advertencia')
]
