from django import forms

class ServicioFormulario(forms.Form):

    nombre= forms.CharField(required=True)

class ProfesionalesFormulario(forms.Form):

   nombre= forms.CharField(required=True)   
   apellido= forms.CharField(required=True)   
   email= forms.EmailField(required=True)

class UsuariosFormulario(forms.Form):

   nombre= forms.CharField(required=True)   
   apellido= forms.CharField(required=True)   
   email= forms.EmailField(required=True)