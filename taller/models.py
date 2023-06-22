from django.conf import settings
from django.db import models
from django.utils import timezone

class Reserva(models.Model):
    Rut = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=50)
    Telefono = models.IntegerField()
    Email = models.CharField(max_length=50)
    Detalle = models.CharField(max_length=500)
    Fecha_Reserva = models.DateTimeField(blank=True, null=True)

    def clean(self):
        if self.fecha_reserva < timezone.now().date():
            raise ValidationError('La fecha de reserva debe ser posterior a la fecha actual.')



#python manage.py makemigrations
#python manage.py migrate