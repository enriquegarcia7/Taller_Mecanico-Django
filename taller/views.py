from django.shortcuts import render,redirect , get_object_or_404 
from .forms import ReservaForm , TrabajoForm , CustomUserCreationForm
from .models import Trabajo
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def index(request):
    return render(request, 'taller/Index.html', {})

def login(request):
    return render(request, 'registration/Login.html', {})

def agendar(request):
    data = {
        'form': ReservaForm()
    }
    if request.method == 'POST':
        formulario = ReservaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Reserva realizada!"
        else:
            data["form"] = formulario
            
    return render(request, 'taller/Agendar.html', data)

def trabajos(request):
    return render(request, 'taller/Trabajos.html', {})

def nosotros(request):
    return render(request, 'taller/Nosotros.html', {})

def registro(request):
    data = {
        'form':CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Te has registrado correctamente")            
            return redirect(to="login")       
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

def base(request):
    return render(request, 'taller/Base.html', {})

@permission_required('taller.change_trabajo')
def administrador(request):
    trabajos = Trabajo.objects.all()

    data = {
        'trabajos' : trabajos 
    }
    return render(request, 'taller/Administrador.html',data)

@permission_required('taller.add_trabajo')    
def mecanico(request):
    data = {
        'form': TrabajoForm()
    }

    if request.method == 'POST':
        formulario = TrabajoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Trabajo Agregado"
        else:
            data["form"] = formulario

    return render(request, 'taller/Mecanico.html', data)

def index2(request):
    return render(request, 'taller/Index2.html', {})

def administrador2(request):
    trabajos = Trabajo.objects.all()

    data = {
        'trabajos' : trabajos 
    }
    return render(request, 'taller/Administrador2.html',data)

def editmecanico(request,id):

    trabajo = get_object_or_404(Trabajo, id=id)

    data = {
        'form': TrabajoForm(instance=trabajo)
    }
    if request.method == 'POST':
        formulario = TrabajoForm(data=request.POST, files=request.FILES , instance=trabajo)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Editado Correctamente"
            return redirect(to="administrador2")
        else:
            data["form"] = formulario

    return render(request, 'taller/EditMecanico.html', data)


def eliminar(request,id):
    trabajo = get_object_or_404(Trabajo, id=id)
    trabajo.delete()
    return redirect(to="administrador2")