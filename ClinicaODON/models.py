from django.db import models

# Create your models here.

class Servicios(models.Model):
   nombre= models.CharField(max_length=50)
   camada= models.IntegerField()

class Profesionales(models.Model):
   nombre= models.CharField(max_length=30)
   apellido= models.CharField(max_length=30)
   email= models.EmailField(null=True)

   def __str__(self):
      return f'{self.nombre}{self.apellido}'

class Usuarios(models.Model):
   nombre= models.CharField(max_length=30)
   apellido= models.CharField(max_length=30)
   email= models.EmailField(null=True)