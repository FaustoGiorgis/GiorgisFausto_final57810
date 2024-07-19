from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    empresa = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.apellido} , {self.empresa}"

class InformeSectorial(models.Model):
    sector = models.CharField(max_length=50)
    informesDisponibles = models.BooleanField()
    UltimaPublicacion = models.DateField()

    def __str__(self):
        return f"{self.sector} , {self.UltimaPublicacion}"
    
   
class Prensa(models.Model):
    TituloNoticia = models.CharField(max_length=50)
    medio = models.CharField(max_length=50)
    LinkNoticia = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.TituloNoticia} , {self.medio}"
    
    
class MonitorMacro(models.Model):
    nombre = models.CharField(max_length=50)
    mesAnalizado = models.CharField(max_length=50)
    fechaPublicacion = models.DateField()

    def __str__(self):
        return f"{self.nombre} , {self.mesAnalizado}"


class Avatar(models.Model):   
    imagen = models.ImageField(upload_to="avatares") 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"  