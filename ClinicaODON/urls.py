from django.urls import path
from ClinicaODON.views import inicio, servicio, lista_servicios, inicio, servicios, profesionales, usuarios, profesionales_formulario, servicio_formulario, usuarios_formulario, busquedaServicio, buscar

urlpatterns = [
    path('agrega-servicio/<nombre>', servicio),
    path('lista-servicios/', lista_servicios),
    path('', inicio),
    path('servicios/', servicios, name='servicios'),
    path('profesionales/', profesionales),
    path('usuarios/', usuarios),
    path('profesionales-formulario/', profesionales_formulario, name= 'ProfesionalesFormulario'),
    path('servicio-formulario/', servicio_formulario, name= 'ServicioFormulario'),
    path('usuarios-formulario/', usuarios_formulario, name= 'UsuariosFormulario'),
    path('busqueda-servicio/', busquedaServicio, name="BusquedaServicio"),
    path('buscar/', buscar, name="Buscar"),
]