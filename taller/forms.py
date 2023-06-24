from django import forms
from .models import Reserva , Trabajo

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'


class TrabajoForm(forms.ModelForm):
   class Meta:
        model = Trabajo
        fields = '__all__'