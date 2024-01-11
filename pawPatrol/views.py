from django.shortcuts import render
from pawPatrol.models import *
from pawPatrol.forms import *
from django.http import HttpResponse
# Create your views here.

def inicio(request):

    return render(request, "inicio.html")

def heroes_principales(request):
    mis_herores = heroe.objects.all()   
    info = {"heroes": mis_herores}
    return render(request, "heroes.html", info)

def villanos(request):
    return render(request, "villanos.html")

def vehiculos(request):
    return render(request, "vehiculos.html")


def comencemos(request):
    return render(request, "comencemos.html")

def padre(request):
    return render(request, "padre.html")

def crearHeroe(request):
    return render(request, "crearheroe.html")

def heroes(request):
    return render(request, "heroes.html")

def agregarHeroe(request):
    
    if request.method == "POST":
        nuevo_form = formularioHeroes(request.POST) #obtiene los datos
        if nuevo_form.is_valid():
            info = nuevo_form.cleaned_data #para tenerlo en modo diccionario
            nuevoHeroe = heroe(nombre=info["nombre"], raza=info["raza"], 
                               habilidad=info["habilidad"], vehiculo=info["vehiculo"])
            nuevoHeroe.save()
            return render(request, "heroes.html")
    else:
        nuevo_form = formularioHeroes()

    return render(request, "formheroe.html", {"nuevoheroe":nuevo_form})

def agregarVillano(request):
    
    if request.method == "POST":
        formV = formularioVillano(request.POST) #obtiene los datos
        if formV.is_valid():
            info = formV.cleaned_data #para tenerlo en modo diccionario
            nuevoVillano = villanos(nombre=info["nombre"], raza=info["raza"], 
                                     vehiculo=info["vehiculo"])
            nuevoVillano.save()
            return render(request, "villlanos.html")
    else:
        formV = formularioVillano()

    return render(request, "formvillano.html", {"nuevovillano":formV})

def agregarVehiculo(request):
    
    if request.method == "POST":
        formVehiculo = formularioVehiculo(request.POST) #obtiene los datos
        if formVehiculo.is_valid():
            info = formVehiculo.cleaned_data #para tenerlo en modo diccionario
            nuevoVehiculo = vehiculo(modelo=info["modelo"],propietario=info["propietario"])
            nuevoVehiculo.save()
            return render(request, "vehiculos.html")
    else:
        formVehiculo = formularioVehiculo()

    return render(request, "formvehiculo.html", {"nuevovehiculo":formVehiculo})


def imagenes(request):

    return render(request, "imagenes.html")

def heroesdos(request):

    return render(request, "heroessig.html")

def vehiculodos(request):

    return render(request, "vehiculossig.html")

def buscarheroe(request):

    return render(request, "buscarheroe.html")


def resultados(request):
    if request.method == "GET":

        pedido = request.GET["nombre"]
        resultado = heroe.objects.filter(nombre__icontains=pedido)

        return render(request, "resultados.html", {"nombre":resultado})
    else:
        respuesta= "No existen datos"
        return HttpResponse(respuesta)
 
