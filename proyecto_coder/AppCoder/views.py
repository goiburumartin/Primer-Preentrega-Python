from django.shortcuts import render,  HttpResponse
from django.http.request import QueryDict
from AppCoder.models import *
from django.http import HttpResponse
from AppCoder.forms import EventoFormulario, PaginaFormulario, SeguidorFormulario


def seguidores(request):
    if request.method == 'POST':

            miFormulario = SeguidorFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:   

                informacion = miFormulario.cleaned_data

                seguidores = Seguidores(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email']) 

                seguidores.save()

                return render(request, "AppCoder/inicio.html") 

    else: 

            miFormulario= SeguidorFormulario()

    return render(request, "AppCoder/Seguidores.html", {"miFormulario":miFormulario})
#def seguidores(request):

#    seguidores = Seguidores(nombre="Martins",apellido="Herrera", email="martinh123@gmail.com")
#    seguidores.save()

#    documentoDeTexto = f"--->seguidor: {seguidores.nombre} {seguidores.apellido}, email: {seguidores.email}"

#    return HttpResponse(documentoDeTexto)


def inicio(request):

    return render(request, "AppCoder/Inicio.html")

def eventos(request):
    if request.method == 'POST':

            miFormulario = EventoFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:  

                informacion = miFormulario.cleaned_data

                eventos = Eventos(nombre=informacion['nombre'], tema=informacion['tema'], integrantes=informacion['integrantes'],
                fechaini=informacion['fechaini'], fechafin=informacion['fechafin']) 

                eventos.save()

                return render(request, "AppCoder/inicio.html") 
    else: 

            miFormulario= EventoFormulario() 

    return render(request, "AppCoder/Eventos.html", {"miFormulario":miFormulario})

# PAGINAS

def paginas(request):
    if request.method == 'POST':

            miFormulario = PaginaFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:   

                informacion = miFormulario.cleaned_data

                paginas = Paginas(nombre=informacion['nombre'], tema=informacion['tema'], integrantes=informacion['integrantes']) 

                paginas.save()

                return render(request, "AppCoder/inicio.html") 

    else: 

            miFormulario= PaginaFormulario()

    return render(request, "AppCoder/Paginas.html", {"miFormulario":miFormulario})

def buscar_pagina(request):

    data =  request.GET.get("tema", '')

    error = ''

    if data:
        try:
            pagina = Paginas.objects.get(tema = data)

            return render(request,"AppCoder/inicio.html",{"pagina":pagina , "tema":data})
        
        except Exception as exc:
            error = "no se encontro la pagina"
    
    return render (request, "AppCoder/inicio.html", {"error": error})