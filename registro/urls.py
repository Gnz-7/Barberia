from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('salir/', views.salir, name='salir')
]