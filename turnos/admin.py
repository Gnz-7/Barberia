from django.contrib import admin
from .models import Lunes, Martes, Miercoles, Jueves, Viernes, Sabado



class LunesAdmin(admin.ModelAdmin):
    list_display = ('horario', 'get_cliente',)
    search_fields = ('horario', 'cliente__username',)
    list_filter = ('horario', 'cliente',)
    ordering = ('horario',)

    def get_cliente(self, obj):
        return obj.cliente.username if obj.cliente else "—"
    get_cliente.short_description = 'Cliente'
    
admin.site.register(Lunes,LunesAdmin)

# -------------------------------------------------------------------------------------------------------

class MartesAdmin(admin.ModelAdmin):
    list_display = ('horario', 'cliente',)
    search_fields = ('horario', 'cliente__username',)
    list_filter = ('horario',)
    ordering = ('horario',)

    def get_cliente(self, obj):
        return obj.cliente.username if obj.cliente else "—"
    get_cliente.short_description = 'Cliente'
    
admin.site.register(Martes,MartesAdmin)

# -------------------------------------------------------------------------------------------------------

class MiercolesAdmin(admin.ModelAdmin):
    list_display = ('horario', 'cliente',)
    search_fields = ('horario', 'cliente__username',)
    list_filter = ('horario',)
    ordering = ('horario',)

    def get_cliente(self, obj):
        return obj.cliente.username if obj.cliente else "—"
    get_cliente.short_description = 'Cliente'
    
admin.site.register(Miercoles,MiercolesAdmin)

# -------------------------------------------------------------------------------------------------------

class JuevesAdmin(admin.ModelAdmin):
    list_display = ('horario', 'cliente',)
    search_fields = ('horario', 'cliente__username',)
    list_filter = ('horario',)
    ordering = ('horario',)

    def get_cliente(self, obj):
        return obj.cliente.username if obj.cliente else "—"
    get_cliente.short_description = 'Cliente'
    
admin.site.register(Jueves,JuevesAdmin)

# -------------------------------------------------------------------------------------------------------

class ViernesAdmin(admin.ModelAdmin):
    list_display = ('horario', 'cliente',)
    search_fields = ('horario', 'cliente__username',)
    list_filter = ('horario',)
    ordering = ('horario',)

    def get_cliente(self, obj):
        return obj.cliente.username if obj.cliente else "—"
    get_cliente.short_description = 'Cliente'
    
admin.site.register(Viernes,ViernesAdmin)

# -------------------------------------------------------------------------------------------------------

class SabadoAdmin(admin.ModelAdmin):
    list_display = ('horario', 'cliente',)
    search_fields = ('horario', 'cliente__username',)
    list_filter = ('horario',)
    ordering = ('horario',)

    def get_cliente(self, obj):
        return obj.cliente.username if obj.cliente else "—"
    get_cliente.short_description = 'Cliente'
    
admin.site.register(Sabado,ViernesAdmin)

# -------------------------------------------------------------------------------------------------------