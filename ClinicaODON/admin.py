from django.contrib import admin
from .models import Servicios, Profesionales, Usuarios, Avatar
# Register your models here.
admin.site.register(Servicios)
admin.site.register(Profesionales)
admin.site.register(Usuarios)
admin.site.register(Avatar)
