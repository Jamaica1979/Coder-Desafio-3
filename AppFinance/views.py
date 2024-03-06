from django.shortcuts import render
from django.http import HttpResponse
from AppFinance.models import Usuario, Ingreso, Egreso
from AppFinance.form import *

# Create your views here

def inicio(request):

    return render (request, "AppFinance/inicio.html")

def ver_usuario(request):
    
    return render (request, "AppFinance/ver_usuario.html")

def ver_ingreso(request):

    return render(request,"AppFinance/ver_ingreso.html")

def ver_egreso(request):

    return render(request,"AppFinance/ver_egreso.html")

def crear_usuario(request):

    if request.method == "POST": 

        usuario_nuevo = Usuario(nombre=request.POST["nombre"], apellido=request.POST['apellido'], email=request.POST['email'], edad=request.POST['edad'])
        usuario_nuevo.save()
    
        return render(request, "AppFinance/inicio.html")

    return render(request,'AppFinance/crear_usuario.html')

def crear_ingreso(request):
    
    if request.method == "POST":

       formulario = form_ingreso(request.POST)

       if formulario.is_valid():
    
            info_dict = formulario.cleaned_data

            ingreso_nuevo = Ingreso (
                fecha = info_dict["fecha"],
                importe = info_dict["importe"],
                categoria = info_dict["categoria"],
                descripcion = info_dict["descripcion"],
            )

            ingreso_nuevo.save()

            return render(request, "AppFinance/inicio.html")
        
    else:
        formulario = form_ingreso

    return render(request,'AppFinance/crear_ingreso.html',{'form': formulario})


def crear_egreso(request):

    if request.method == "POST":

       formulario = form_egreso(request.POST)

       if formulario.is_valid():
    
            info_dict = formulario.cleaned_data

            egreso_nuevo = Egreso (
                fecha = info_dict["fecha"],
                importe = info_dict["importe"],
                categoria = info_dict["categoria"],
                descripcion = info_dict["descripcion"],
            )
            egreso_nuevo.save()

            return render(request, "AppFinance/inicio.html")
        
    else:
        formulario = form_egreso()
    
    return render(request,'AppFinance/crear_egreso.html', {'form': formulario})

def buscar_usuario(request):
    
    return render(request, "AppFinance/buscar_usuario.html")

def resultados_usuario(request):
    
    usuario = request.GET['nombre']

    resultados = Usuario.objects.filter(nombre__iexact=usuario)

    return render (request, "AppFinance/resultados.html",{'resultados':resultados})






