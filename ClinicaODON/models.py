from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Servicios(models.Model):
   nombre= models.CharField(max_length=50)
   
   def __str__(self):
      return f'{self.nombre}'

class Profesionales(models.Model):
   nombre= models.CharField(max_length=30)
   apellido= models.CharField(max_length=30)
   email= models.EmailField(null=True)

   def __str__(self):
      return f'{self.nombre} {self.apellido}'

class Usuarios(models.Model):
   nombre= models.CharField(max_length=30)
   apellido= models.CharField(max_length=30)
   email= models.EmailField(null=True)

class Avatar (models.Model):

   user= models.ForeignKey(User, on_delete=models.CASCADE)  
   imagen = models.ImageField(upload_to= 'avatares', blank= True, null= True)