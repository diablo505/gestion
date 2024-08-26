from datetime import timezone

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now

from validadores import  validar_te
class CamposEnMayusculas(models.CharField):
    def __init__(self, *args, **kwargs):
        super(CamposEnMayusculas, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        # return str(value).lower()
        return str(value).upper()

def validar_fecha_en_el_futuro(value):
    if value > now():
        raise ValidationError('La novedad no puede registrarse en el futuro')


class cliente(models.Model):
    nombre = CamposEnMayusculas(max_length=50, verbose_name="Nombre del cliente", null=False,
                                  blank=False, unique=True,
                                  error_messages={'unique': 'Ya existe un cliente con ese nombre.'})
    nro_tel= models.nro_tel = models.CharField(max_length=30, validators=[validar_te], null=True, blank=False,
                               verbose_name='Número de teléfono celular')

    direccion = CamposEnMayusculas(max_length=50, verbose_name="Dirección", null=False,
                                  blank=False, unique=False,
                                  )
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombre
class tipo_actividad(models.Model):
    tipo = CamposEnMayusculas(max_length=50, verbose_name="Tipo", null=False,
                                  blank=False, unique=True,
                                  error_messages={'unique': 'Ya existe un Tipo de actividad con ese nombre.'})
    class Meta:
        verbose_name = 'Tipo de actividad'
        verbose_name_plural = 'Tipos de actividad'

    def __str__(self):
        return self.tipo


SITUACION = (
        ('PARA PRESUPUESTAR','PARA PRESUPUESTAR'),
        ('PRESUPUESTADO','PRESUPESTADO'),
        ('PLANIFICADO','PLANIFICADO'),
        ('TERMINADO', 'TERMINADO'),
    )
class actividad(models.Model):
    estado= models.CharField(max_length=30, choices=SITUACION,
                                 blank=False, null=True, default='PRESUPUESTADO')
    fecha = models.DateTimeField(
        verbose_name='Fecha', blank=False, null=False, default=now, validators=[validar_fecha_en_el_futuro])
    tipo = models.ForeignKey(tipo_actividad,related_name='actividad_tipo',
                              on_delete=models.PROTECT, blank=False, null=True)
    cliente = models.ForeignKey(cliente, related_name='cliente_actividad',
                                on_delete=models.PROTECT, blank=False, null=True)
    detalle = CamposEnMayusculas(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Lista de Actividades'
    def __str__(self):
        return "%s - %s" % (self.cliente, self.fecha)