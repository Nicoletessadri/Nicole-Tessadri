from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Servicios, Profesionales, Usuarios
from .forms import ServicioFormulario, ProfesionalesFormulario, UsuariosFormulario


# Create your views here.

def servicio(req, nombre):

    servicio= Servicios(nombre=nombre)
    servicio.save()
    return HttpResponse (f"""
             <p>Servicio: {servicio.nombre} agregado! </p>  
                   """)
    curso.save
def lista_servicios (req):

    lista = Servicios.objects.all()

    return render(req, "lista_servicios.html" , {"lista_servicios": lista})

def inicio(req):
    return render(req, "inicio.html")
   
def servicios(req):
    return render(req, "servicios.html")

def profesionales(req):
    return render(req, "profesionales.html")

def usuarios(req):
    return render(req, "usuarios.html")

def servicio_formulario(req: HttpRequest):

    print ('method', req.method)
    print('post', req.POST)

    if req.method== 'POST':

        miFormulario2= ServicioFormulario(req.POST)

        if miFormulario2.is_valid():

            print (miFormulario2.cleaned_data)
            data= miFormulario2.cleaned_data

            servicio = Servicios (nombre= data["nombre"])
            servicio.save()
            return render(req, "inicio.html", {"mensaje": "Servicio creado con exito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario invalido"})
    else :
        miFormulario2=  ServicioFormulario()
        return render(req, "servicio_formulario.html", {"miFormulario2": miFormulario2})
    
def profesionales_formulario(req: HttpRequest):

    print ('method', req.method)
    print('post', req.POST)

    if req.method== 'POST':

        miFormulario= ProfesionalesFormulario(req.POST)

        if miFormulario.is_valid():

            print (miFormulario.cleaned_data)
            data= miFormulario.cleaned_data

            profesional = Profesionales(nombre= data["nombre"], apellido= data["apellido"], email = data["email"])
            profesional.save()
            return render(req, "inicio.html", {"mensaje": "Profesional creado con exito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario invalido"})
    else :
        miFormulario=  ProfesionalesFormulario()
        return render(req, "profesionales_formulario.html", {"miFormulario": miFormulario})
    
def usuarios_formulario(req: HttpRequest):

    print ('method', req.method)
    print('post', req.POST)

    if req.method== 'POST':

        miFormulario3= UsuariosFormulario(req.POST)

        if miFormulario3.is_valid():

            print (miFormulario3.cleaned_data)
            data= miFormulario3.cleaned_data

            usuario = Usuarios (nombre= data["nombre"], apellido= data["apellido"], email = data["email"])
            usuario.save()
            return render(req, "inicio.html", {"mensaje": "Usuario creado con exito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Usuario invalido"})
    else :
        miFormulario3=  UsuariosFormulario()
        return render(req, "usuarios_formulario.html", {"miFormulario3": miFormulario3})
    
def busquedaServicio(req):

    return render(req, "busquedaServicio.html")

def buscar(req):
 
    if req.GET["servicio"]:
        nombre= req.GET["servicio"]
        servicio= Servicios.objects.get(nombre=nombre)
        if servicio:
            return render(req, "resultadoBusqueda.html", {"servicio": servicio})
        else:
            return HttpResponse(f"No escribiste ningun servicio")