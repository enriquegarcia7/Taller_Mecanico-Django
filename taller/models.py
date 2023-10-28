from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Reserva(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()
    detalle = models.CharField(max_length=2000)
    fecha = models.DateField()

    def __str__(self):
        return f"Reserva: {self.nombre} ({self.fecha})"


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
    imagen = models.ImageField(upload_to='trabajos', null=True) 
    mensaje = models.TextField()


    def __str__(self):
        return self.mecanico

class Servicio(models.Model):
    Cod = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=100)
    Costo = models.IntegerField()   



    def __str__(self):
        return self.rut

class Producto(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    costo = models.IntegerField()
    proveedor = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    fecha = models.DateField(default=timezone.now)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.proveedor