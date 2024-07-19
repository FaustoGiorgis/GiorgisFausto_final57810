from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class clienteForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email= forms.EmailField(max_length=50, required=True)
    empresa = forms.CharField(max_length=50, required=True)

class prensaForm(forms.Form):
    TituloNoticia = forms.CharField(label="Titulo Noticia", max_length=50, required=True)
    medio = forms.CharField(label="Medio", max_length=50, required=True)
    LinkNoticia = forms.CharField(label="Link a noticia", max_length=50, required=True)

class informesForm(forms.Form):
    sector = forms.CharField(label="Sector", max_length=50, required=True)
    informesDisponibles = forms.BooleanField(label="¿Está disponible en 2024?", required=True)
    UltimaPublicacion = forms.DateField(label="Última publicación", required=True)

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre", max_length=30, required=True)
    last_name = forms.CharField(label="Apellido", max_length=30, required=True)


    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]



class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)