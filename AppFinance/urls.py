from django.urls import path
from AppFinance.views import *



urlpatterns = [

    path('', inicio, name= 'Inicio'),
    path('usuario/', ver_usuario, name='Usuario'),
    path('ingreso/', ver_ingreso, name='Ingreso'),
    path('egreso/', ver_egreso,name='Egreso'),
    path('crear_usuario/', crear_usuario, name='Usuario'),
    path('crear_ingreso/', crear_ingreso, name= 'Ingreso'),
    path('crear_egreso/', crear_egreso, name='Egreso'),
    path('buscar_usuario/', buscar_usuario, name='Buscar'),
    path('resultados/', resultados_usuario, name='Resultados'),




]
