from django.urls import path
from . import views



urlpatterns = [
    path('mis_turnos/', views.mis_turnos, name='mis_turnos'),
    path('ver_perfil/<int:usuario_id>/', views.ver_perfil, name='ver_perfil'),
    path('editar/<int:usuario_id>/', views.editar, name='editar'),
    path('cambiar_password/<int:usuario_id>/', views.cambiar_password, name='cambiar_password' ),
]
