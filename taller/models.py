from django.conf import settings
from django.db import models
from django.utils import timezone

class Reserva(models.Model):
    Rut = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=200)
    Telefono = models.TextField()
    Hora_Actual = models.DateTimeField(default=timezone.now)
    Fecha_Reserva = models.DateTimeField(blank=True, null=True)

    def hora_actual(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models 