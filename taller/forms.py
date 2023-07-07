from django import forms
from .models import Reserva , Trabajo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'


class TrabajoForm(forms.ModelForm):
   class Meta:
        model = Trabajo
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username',"first_name","last_name","email",'password1',"password2"]