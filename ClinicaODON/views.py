from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Servicios, Profesionales, Usuarios, Avatar
from .forms import ServicioFormulario, ProfesionalesFormulario, UsuariosFormulario, UserEditForm, AvatarFormulario
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.list import ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

@staff_member_required(login_url='/ClinicaODO/autorizacion')
def servicio(req, nombre):

    servicio= Servicios(nombre=nombre)
    servicio.save()
    return HttpResponse (f"""
             <p>Servicio: {servicio.nombre} agregado! </p>  
                   """)
    curso.save

@login_required
def lista_servicios (req):

    lista = Servicios.objects.all()

    return render(req, "lista_servicios.html" , {"lista_servicios": lista})

def inicio(req):

    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "inicio.html", {"url": avatar.imagen.url})
    except:
        return render(req, "inicio.html")

   
def servicios(req):
    return render(req, "servicios.html")

@login_required
def profesionales(req):
    return render(req, "profesionales.html")

@login_required
def usuarios(req):
    return render(req, "usuarios.html")

@staff_member_required(login_url='/ClinicaODO/autorizacion')
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

@staff_member_required(login_url='/ClinicaODO/autorizacion')
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


@staff_member_required(login_url='/ClinicaODO/autorizacion')
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

@login_required
def listaProfesionales(req):

    profesionales= Profesionales.objects.all()
    return render(req, "leerProfesionales.html", {"profesionales": profesionales})

@staff_member_required(login_url='/ClinicaODO/autorizacion')    
def eliminarProfesional(req, id):

    if req.method == 'POST':

        profesional= Profesionales.objects.get(id=id)
        profesional.delete()
        
        profesionales= Profesionales.objects.all()
        
        return render(req, "leerProfesionales.html", {"profesionales": profesionales})

@staff_member_required(login_url='/ClinicaODO/autorizacion')
def editarProfesional(req, id):

    profesional= Profesionales.objects.get(id=id)

    if req.method== 'POST':

        miFormulario= ProfesionalesFormulario(req.POST)

        if miFormulario.is_valid():

            data= miFormulario.cleaned_data

            profesional.nombre= data["nombre"]
            profesional.apellido= data["apellido"]
            profesional.email= data["email"]
            profesional.save()
            return render(req, "inicio.html", {"mensaje": "Profesional actualizado con exito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario invalido"})
    else :
        miFormulario=  ProfesionalesFormulario(initial= {
            "nombre": profesional.nombre,
            "apellido": profesional.apellido,
            "email": profesional.email})
        
        return render(req, "editarProfesional.html", {"miFormulario": miFormulario, "id": profesional.id})


class ServicioList(ListView):
    model = Servicios
    template_name = "servicio_list.html"
    context_object_name= "servicios"


class ServicioDetail(LoginRequiredMixin, DetailView):
    model = Servicios
    template_name = "servicio_detail.html"
    context_object_name= "servicio"


class ServicioCreate(LoginRequiredMixin, CreateView):
    model = Servicios
    template_name = "servicio_create.html"
    fields= ["nombre"]
    success_url= "/ClinicaODO/"
    


class ServicioUpdate(LoginRequiredMixin, UpdateView):
    model = Servicios
    template_name = "servicio_update.html"
    fields= ("__all__")
    success_url= "/ClinicaODO/"
    context_object_name= "servicio"


class ServicioDelete(LoginRequiredMixin, DeleteView):
    model = Servicios
    template_name = "servicio_delete.html"
    success_url= "/ClinicaODO/"

def loginView(req):
    
    if req.method== 'POST':
         
        miFormulario=AuthenticationForm(req, data=req.POST)
        
        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user= authenticate(username=usuario, password=psw)
            
            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(req, "inicio.html", {"mensaje": "Datos incorrectos"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario invalido"})

    else:
        miFormulario= AuthenticationForm()
        return render(req, "login.html", {"miFormulario": miFormulario}) 


def register(req):
        
        if req.method == 'POST':
         
            miFormulario = UserCreationForm(req.POST)
        
            if miFormulario.is_valid():

                data = miFormulario.cleaned_data

                usuario= data["username"]

                miFormulario.save()
                
                return render(req, "inicio.html", {"mensaje":f"Usuario {usuario} creado con exito"})
                
            else:
                return render(req, "inicio.html", {"mensaje": "Formulario invalido"})

        else:
            miFormulario= UserCreationForm()
            return render(req, "registro.html", {"miFormulario": miFormulario}) 
        
def autorizacion(req):
    return render(req, "autorizacion.html")

@staff_member_required(login_url='/ClinicaODO/autorizacion')
def editar_perfil(req):
    
    usuario = req.user

    if req.method == 'POST':

        miFormulario= UserEditForm(req.POST, instance=req.user)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()
            return render(req, "inicio.html", {"mensaje": "Perfil actualizado con exito"})
        else:
            return render(req, "editarPerfil.html", {"miFormulario": miFormulario})
    else :
        miFormulario=  UserEditForm(instance = req.user)
        
        return render(req, "editarPerfil.html", {"miFormulario": miFormulario})

@login_required
def agregarAvatar(req):
       
    if req.method == 'POST':
         
            miFormulario = AvatarFormulario(req.POST, req.FILES)
        
            if miFormulario.is_valid():

                data = miFormulario.cleaned_data

                avatar= Avatar (user= req.user , imagen= data["imagen"])

                avatar.save()
                
                return render(req, "inicio.html", {"mensaje":f"Avatar actualizado con exito"})
                
            else:
                return render(req, "inicio.html", {"mensaje": "Formulario invalido"})
        
    else:

            miFormulario= AvatarFormulario()
            return render(req, "agregarAvatar.html", {"miFormulario": miFormulario}) 
        