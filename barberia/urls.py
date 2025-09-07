from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='index.html'), name='index'),
    path('registro/', include('registro.urls')),
    path('turnos/', include('turnos.urls'))
]
