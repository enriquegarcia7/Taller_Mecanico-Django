from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name='index'),
     path('login/', views.login, name='login'),
     path('login2/', views.login, name='login2'),
     path('agendar/', views.agendar, name='agendar'),
     path('trabajos/', views.trabajos, name='trabajos'),
     path('nosotros/', views.nosotros, name='nosotros'),
     path('registro/', views.registro, name='registro'),
     path('base/', views.base, name='base'),
]
