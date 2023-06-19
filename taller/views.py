from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'taller/Index.html', {})

def login(request):
    return render(request, 'taller/Login.html', {})

def agendar(request):
    return render(request, 'taller/Agendar.html', {})

def trabajos(request):
    return render(request, 'taller/trabajos.html', {})

def nosotros(request):
    return render(request, 'taller/Nosotros.html', {})

def registro(request):
    return render(request, 'taller/Registro.html', {})

def base(request):
    return render(request, 'taller/Base.html', {})

def login2(request):
    return render(request, 'taller/Login2.html', {})