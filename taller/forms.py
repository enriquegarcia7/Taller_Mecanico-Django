from django import forms

from .models import Reserva , Trabajo


class TrabajoForm(forms.ModelForm):
   class Meta:
        model = Trabajo
        fields = '__all__'