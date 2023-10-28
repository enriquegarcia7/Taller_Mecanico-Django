from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name='index'),     
     path('agendar/', views.agendar, name='agendar'),
     path('trabajos/', views.trabajos, name='trabajos'),
     path('nosotros/', views.nosotros, name='nosotros'),
     path('registro/', views.registro, name='registro'),
     path('base/', views.base, name='base'),
     path('mecanico/', views.mecanico, name='mecanico'),
     path('administrador/', views.administrador, name='administrador'),     
     path('editmecanico/<id>', views.editmecanico, name='editmecanico'),
     path('eliminar/<id>', views.eliminar, name='eliminar'),
     path('agenda/', views.agenda, name='agenda'),      
     path('generar_orden_pedido_pdf/', views.generar_orden_pedido_pdf, name='generar_orden_pedido_pdf'),
     path('agregar-producto/', views.agregar_producto,name='agregar_producto'),
     path('listar/', views.listar, name='reportes'),
     path('modificar/<id>', views.modificar, name='modificar'),
     path('eliminar/<id>', views.eliminar, name='eliminar'),
]
