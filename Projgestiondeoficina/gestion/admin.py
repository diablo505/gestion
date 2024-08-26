from django.contrib import admin
from gestion.models import cliente, tipo_actividad,actividad
from django.db import models
from django import forms
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre','nro_tel','direccion')

admin.site.register(cliente, ClientesAdmin)

class Tipo_actAdmin(admin.ModelAdmin):
    list_display = ('tipo',)

admin.site.register(tipo_actividad, Tipo_actAdmin)

class ActividadAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'tipo', 'cliente')
    search_fields = ['fecha','tipo','cliente']
    formfield_overrides = {
        models.CharField: {
            'widget': forms.TextInput(attrs={'size': '100'})
        },
        }
    def get_cliente(self, obj):
        return obj.cliente
admin.site.register(actividad, ActividadAdmin)