from django.urls import path
from . import views



urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),   
    path('lunes/', views.lunes, name='lunes'), 
    path('martes/', views.martes, name='martes'),  
    path('miercoles/', views.miercoles, name='miercoles'),   
    path('jueves/', views.jueves, name='jueves'),  
    path('viernes/', views.viernes, name='viernes'),
    path('sabado/', views.sabado, name='sabado'),
]
