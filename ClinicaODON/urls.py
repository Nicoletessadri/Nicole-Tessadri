from django.urls import path
from django.contrib.auth.views import LogoutView
from ClinicaODON.views import inicio, servicio, lista_servicios, inicio, servicios, profesionales, usuarios, profesionales_formulario, servicio_formulario, usuarios_formulario, busquedaServicio, buscar, listaProfesionales, eliminarProfesional, editarProfesional, ServicioList, ServicioCreate, ServicioDetail, ServicioDelete, ServicioUpdate, loginView, register, autorizacion, editar_perfil, agregarAvatar, AboutMe, contact, user_detail
urlpatterns = [
    path('agrega-servicio/<nombre>', servicio),
    path('lista-servicios/', lista_servicios),
    path('', inicio, name= 'Inicio'),
    path('servicios/', servicios, name='servicios'),
    path('profesionales/', profesionales),
    path('usuarios/', usuarios),
    path('profesionales-formulario/', profesionales_formulario, name= 'ProfesionalesFormulario'),
    path('servicio-formulario/', servicio_formulario, name= 'ServicioFormulario'),
    path('usuarios-formulario/', usuarios_formulario, name= 'UsuariosFormulario'),
    path('busqueda-servicio/', busquedaServicio, name="BusquedaServicio"),
    path('buscar/', buscar, name="Buscar"),
    path('lista-profesionales/', listaProfesionales, name="ListaProfesionales"),
    path('elimina-profesionales/<int:id>', eliminarProfesional, name="EliminarProfesional"),
    path('editar-profesionales/<int:id>', editarProfesional, name="EditarProfesional"),
    path('lista-servicio', ServicioList.as_view(), name="ListaServicios"),
    path('detalle-servicio/<pk>', ServicioDetail.as_view(), name="DetalleServicios"),
    path('crea-servicio', ServicioCreate.as_view(), name="CreaServicios"),
    path('actualizar-servicio/<pk>', ServicioUpdate.as_view(), name="ActualizarServicios"),
    path('eliminar-servicio/<pk>', ServicioDelete.as_view(), name="EliminarServicios"),
    path('login', loginView, name="Login"),
    path('registrar', register, name="Registrar"),
    path('logout', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('autorizacion', autorizacion, name="Autorizacion"),
    path('editar-perfil', editar_perfil, name="EditarPerfil"),
    path('agregar-avatar', agregarAvatar, name="AgregarAvatar"),
    path('aboutme', AboutMe, name="Aboutme"),
    path('contacto', contact, name="Contacto"),
    path('user/detail/',user_detail, name='user_detail')
]