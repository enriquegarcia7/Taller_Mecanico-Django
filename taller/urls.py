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
     path('index2/', views.index2, name='index2'),     
     path('editmecanico/<id>', views.editmecanico, name='editmecanico'),
     path('eliminar/<id>', views.eliminar, name='eliminar'),
]
