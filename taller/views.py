from django.shortcuts import render,redirect , get_object_or_404 
from .forms import ReservaForm , TrabajoForm , CustomUserCreationForm , ServicioForm , Producto2Form, ProductoForm
from .models import Trabajo , Servicio , Reserva , Producto , Producto2
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch 

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
            messages.success(request, "Reserva realizada!")
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


def agenda(request):
    agendas = Reserva.objects.all()

    data = {
        'reservas' : agendas 
    }
    return render(request, 'taller/Agenda.html',data)

def agregarservicios(request):
    data = {
        'form': ServicioForm()
    }
    if request.method == 'POST':
        formulario = ServicioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Servicio Creado con Exito.") 
        else:
            data["form"] = formulario
            
    return render(request, 'taller/AgregarServicios.html', data)

def gestionarservicios(request):
    servicios = Servicio.objects.all()

    data = {
        'servicios' : servicios 
    }
    return render(request, 'taller/GestionarServicios.html',data)


@permission_required('taller.add_trabajo')    
def mecanico(request):
    data = {
        'form': TrabajoForm()
    }

    if request.method == 'POST':
        formulario = TrabajoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Trabajo Agregado")
        else:
            data["form"] = formulario

    return render(request, 'taller/Mecanico.html', data)

@permission_required('taller.change_trabajo')
def editmecanico(request,id):

    trabajo = get_object_or_404(Trabajo, id=id)

    data = {
        'form': TrabajoForm(instance=trabajo)
    }
    if request.method == 'POST':
        formulario = TrabajoForm(data=request.POST, files=request.FILES , instance=trabajo)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado Correctamente")
            return redirect(to="administrador")
        else:
            data["form"] = formulario

    return render(request, 'taller/EditMecanico.html', data)

def edithora(request,id):

    reserva = get_object_or_404(Reserva, id=id)

    data = {
        'form': ReservaForm(instance=reserva)
    }
    if request.method == 'POST':
        formulario = ReservaForm(data=request.POST, instance=reserva)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado Correctamente")
            return redirect(to="agenda")
        else:
            data["form"] = formulario

    return render(request, 'taller/EditHora.html', data)

def editservicio(request,id):

    servicio = get_object_or_404(Servicio, id=id)

    data = {
        'form': ServicioForm(instance=servicio)
    }
    if request.method == 'POST':
        formulario = ServicioForm(data=request.POST, instance=servicio)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado Correctamente")
            return redirect(to="gestionarservicios")
        else:
            data["form"] = formulario

    return render(request, 'taller/EditServicio.html', data)

@permission_required('taller.delete_trabajo')
def eliminar(request,id):
    trabajo = get_object_or_404(Trabajo, id=id)
    trabajo.delete()
    return redirect(to="administrador")

def eliminarhora(request,id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    messages.success(request, "eliminado correctamente!")
    return redirect(to="agenda")

def eliminarservicio(request,id):
    servicio = get_object_or_404(Servicio, id=id)
    servicio.delete()
    messages.success(request, "eliminado correctamente!")
    return redirect(to="gestionarservicios")

def reportes(request):
    productos = Producto.objects.all()
    form = ProductoForm()
    return render(request, 'taller/Reportes.html', {'productos': productos, 'form': form})

def agregar_producto(request):
    data={
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado correctamente")
        else:
            data["form"] = formulario

    return render(request, 'taller/Producto/AgregarProducto.html',  data)

def listar(request):
    productos = Producto.objects.all()

    data= {
    'productos': productos
    }

    return render(request, 'taller/Producto/Listar.html', data)

def modificar(request, id):
    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado Correctamente")
            return redirect(to="reportes")
        else:
            data["form"] = formulario

    return render(request, 'taller/Producto/Modificar.html', data)

def eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect (to="reportes")

def generar_orden_pedido_pdf(request):
    productos = Producto.objects.all()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="orden_de_pedido.pdf"'

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    data = []
    data.append(Paragraph("Orden de Pedido", styles["Title"]))
    data.append(Spacer(1, 12))

    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    table_data = [['Código', 'Nombre del Producto', 'Costo', 'Proveedor', 'Cantidad', 'Fecha']]

    for producto in productos:
        table_data.append([producto.codigo, producto.nombre, str(producto.costo), producto.proveedor, str(producto.cantidad), str(producto.fecha)])

    t = Table(table_data, colWidths=[1 * inch, 2 * inch, 1 * inch, 1 * inch, 1 * inch, 1 * inch])
    t.setStyle(table_style)

    data.append(t)
    doc.build(data)

    response.write(buffer.getvalue())
    buffer.close()
    return response


def inventario(request):
    productos2 = Producto2.objects.all()

    data= {
    'productos2': productos2
    }

    return render(request, 'taller/Inventario/Inventario.html', data)

def modificar(request, id):
    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado Correctamente")
            return redirect(to="inventario")
        else:
            data["form"] = formulario

    return render(request, 'taller/Producto/Modificar.html', data)

def eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect (to="reportes")


def agregarproductoinv(request):
    data={
        'form': Producto2Form()
    }
    if request.method == 'POST':
        formulario = Producto2Form(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado correctamente")
        else:
            data["form"] = formulario

    return render(request, 'taller/Inventario/AgregarProductoInv.html',  data)