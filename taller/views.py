from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'taller/Index.html', {})

def login(request):
    return render(request, 'taller/Login.html', {})

def agendar(request):
    return render(request, 'taller/Agendar.html', {})