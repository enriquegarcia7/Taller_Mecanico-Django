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
     path('edithora/<id>', views.edithora, name='edithora'),  
     path('eliminarhora/<id>', views.eliminarhora, name='eliminarhora'),  
     path('agregarservicios/', views.agregarservicios, name='agregarservicios'), 
     path('gestionarservicios/', views.gestionarservicios, name='gestionarservicios'), 
     path('editservicio/<id>', views.editservicio, name='editservicio'), 
     path('eliminarservicio/<id>', views.eliminarservicio, name='eliminarservicio'), 
]
