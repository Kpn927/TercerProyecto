from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import Template, Context, loader
from .forms import *


def start(request):
    
    return render(request, "principal.html")


def cafes_pendientes(request):
    
    if request.method == "POST":
        
        nuevo_formulario = CafeFormulario(request.POST)
        
        if nuevo_formulario.is_valid():
            
            info = nuevo_formulario.cleaned_data
            cafe_nuevo = Cafe(nombre=info["nombre"])
            cafe_nuevo.save()
            return render(request, "principal.html")
    else:
        nuevo_formulario = CafeFormulario()

    return render(request, "cafes.html", {"formulario":nuevo_formulario})

def registros(request):
    
    if request.method == "POST":
        
        nuevo_formulario = RegisFormulario(request.POST)
        
        if nuevo_formulario.is_valid():
            
            info = nuevo_formulario.cleaned_data
            regis_nuevo = Users(Usuario=info["Usuario"], 
                                Password=info["Password"])
            regis_nuevo.save()
            return render(request, "principal.html")
    else:
        nuevo_formulario = RegisFormulario()
    
    return render(request, "registro.html", {"formulario":nuevo_formulario})

def deliver(request):
    
    if request.method == "POST":
        
        nuevo_formulario = deliverFormulario(request.POST)
        
        if nuevo_formulario.is_valid():
            
            info = nuevo_formulario.cleaned_data
            regis_nuevo = delivery(ubicacion = info["ubicacion"], 
                                   telefono = info["telefono"],
                                   Nombre = info["Nombre"],
                                   Correo = info["Correo"]
                                   )
            regis_nuevo.save()
            return render(request, "principal.html")
    else:
        nuevo_formulario = deliverFormulario()
        
    return render(request, "delivery.html", {"formulario":nuevo_formulario})


    
