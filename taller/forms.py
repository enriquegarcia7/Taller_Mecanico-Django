from django import forms
from .models import Reserva , Trabajo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

class ReservaForm(forms.ModelForm):
    fecha = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'dd/mm/yyyy'})
    )
    class Meta:
        model = Reserva
        fields = '__all__'
        
    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha < timezone.now().date():
            raise ValidationError("La fecha debe ser en el futuro")
        return fecha

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@gmail.com'):
            raise ValidationError("El correo electrónico debe ser de gmail.com")
        return email

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if len(str(telefono)) != 9:
            raise ValidationError("El número de teléfono debe tener 9 dígitos")
        return telefono

class TrabajoForm(forms.ModelForm):
   class Meta:
        model = Trabajo
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username',"first_name","last_name","email",'password1',"password2"]