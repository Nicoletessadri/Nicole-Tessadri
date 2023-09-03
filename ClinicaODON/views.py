from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Servicios, Profesionales


# Create your views here.

def servicio(req, nombre):

    servicio= Servicios(nombre=nombre)
    servicio.save()
    return HttpResponse (f"""
             <p>Curso: {servicio.nombre}agregado! </p>  
                   """)
    curso.save
def lista_servicios (req):

    lista = Servicios.objects.all()

    return render(req, "lista_cursos.html" , {"lista_cursos": lista})
