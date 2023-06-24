from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Reserva(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Rut = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=50)
    Telefono = models.IntegerField()
    Email = models.EmailField(max_length=50)
    Detalle = models.CharField(max_length=500)
    Fecha_Reserva = models.DateTimeField(blank=True, null=True)

    def clean(self):
        if self.Fecha_Reserva.date() < timezone.now().date():
            raise ValidationError('La fecha de reserva debe ser posterior a la fecha actual.')

    def __str__(self):
        return f"Reserva: {self.Nombre} ({self.Fecha_Reserva})"


mecanicos = [
    [0,"PEDRO SOTO - Especialista en Electronica automotriz"],
    [1,"JORGE GONZALEZ - Especialista en Caja de Cambios"],
    [2,"JOSE MUÑOZ - Especialista en Suspención y Dirección"]
]

class Trabajo(models.Model):
    mecanico = models.IntegerField(choices=mecanicos)
    id_vehiculo = models.CharField(max_length=18)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    fecha_atencion = models.DateField(blank=True, null=True)
    imagen = models.ImageField(upload_to='trabajos/', null=True) 
    mensaje = models.TextField()


    def __str__(self):
        return self.id_vehiculo