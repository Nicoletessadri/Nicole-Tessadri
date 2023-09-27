from django import forms
from .models import Servicios, Usuarios, Avatar
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class ServicioFormulario(forms.ModelForm):
   class Meta:
      model = Servicios
      fields = ('__all__')


class ProfesionalesFormulario(forms.Form):

   nombre= forms.CharField(required=True)   
   apellido= forms.CharField(required=True)   
   email= forms.EmailField(required=True)

class UsuariosFormulario(forms.Form):

   nombre= forms.CharField(required=True)   
   apellido= forms.CharField(required=True)   
   email= forms.EmailField(required=True)
   
class UserEditForm(UserChangeForm):

   password= forms.CharField(
      help_text="",
      widget=forms.HiddenInput(), required=False
   )

   password1 = forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
   password2 = forms.CharField(label= "Repita contraseña",  widget=forms.PasswordInput)

   class Meta:
      model = User
      fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

   def clean_password2(self):

      print(self.cleaned_data)

      password2 = self.cleaned_data["password2"]
      if password2 != self.cleaned_data["password1"]:
         raise forms.ValidationError("Las contraseñas no coinciden")
      return password2

class AvatarFormulario (forms.ModelForm):

   class Meta:
      model = Avatar
      fields= ('imagen', )

class ContactForm(forms.Form):
   name= forms.CharField(label= 'Nombre')
   email = forms.EmailField(label= 'Email')
   message= forms.CharField(label= 'Mensaje', widget=forms.Textarea)