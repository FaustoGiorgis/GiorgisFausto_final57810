from django.shortcuts import render, redirect
from entidades.models import *
from entidades.forms import *
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView


# Create your views here.
def home(request):
    return render(request, "entidades/index.html")

def quienesSomos(request):
    return render(request, "entidades/quienesSomos.html")

#_______Clientes_________

def clientes(request):
    contexto = {"Cliente" : Cliente.objects.all()}
    return render(request, "entidades/clientes.html", contexto)

@login_required
def clientesForm(request):
    if request.method == "POST":
        miForm = clienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_apellido = miForm.cleaned_data.get("apellido")
            cliente_email = miForm.cleaned_data.get("email")
            cliente_empresa = miForm.cleaned_data.get("empresa")
            cliente = Cliente(nombre=cliente_nombre, apellido=cliente_apellido,email=cliente_email,empresa=cliente_empresa,)
            cliente.save()
            contexto = {"Cliente" : Cliente.objects.all()}
            return render(request, "entidades/clientes.html", contexto)
    else:   
        miForm = clienteForm()
    return render(request, "entidades/clienteForm.html", {"form" :  miForm}) 

@login_required
def clienteUpdate(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == "POST":
        miForm = clienteForm(request.POST)
        if miForm.is_valid():
            cliente.nombre = miForm.cleaned_data.get("nombre")
            cliente.apellido = miForm.cleaned_data.get("apellido")
            cliente.email = miForm.cleaned_data.get("email")
            cliente.empresa = miForm.cleaned_data.get("empresa")
            cliente.save()
            contexto = {"Cliente": Cliente.objects.all() }
            return render(request, "entidades/clientes.html", contexto)       
    else:
        miForm = clienteForm(initial={"nombre": cliente.nombre, "apellido": cliente.apellido,"email": cliente.email, "empresa": cliente.empresa }) 
    return render(request, "entidades/clienteForm.html", {"form": miForm})

@login_required
def clienteDelete(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    cliente.delete()
    contexto = {"Cliente": Cliente.objects.all() }
    return render(request, "entidades/clientes.html", contexto) 





#_______Prensa_______

def prensa(request):
    contexto = {"prensa" : Prensa.objects.all()}
    return render(request, "entidades/prensa.html", contexto)

@login_required
def PrensaForm(request):
    if request.method == "POST":
        miForm = prensaForm(request.POST)
        if miForm.is_valid():
            prensa_noticia = miForm.cleaned_data.get("TituloNoticia")
            prensa_medio = miForm.cleaned_data.get("medio")
            prensa_link = miForm.cleaned_data.get("LinkNoticia")
            prensa = Prensa(TituloNoticia=prensa_noticia, medio=prensa_medio,LinkNoticia=prensa_link)
            prensa.save()
            contexto = {"prensa" : Prensa.objects.all()}
            return render(request, "entidades/prensa.html", contexto)
    else:   
        miForm = prensaForm()

    return render(request, "entidades/prensa_form.html", {"form" :  miForm}) 

class prensaUpdate(LoginRequiredMixin, UpdateView):
    model = Prensa
    fields = ["TituloNoticia", "medio", "LinkNoticia"]
    success_url = reverse_lazy("prensa")

class prensaDelete(LoginRequiredMixin, DeleteView):
    model = Prensa
    success_url = reverse_lazy("prensa")






#_________Informes Sectoriales ________________

def InformesSectoriales(request):
    contexto = {"informesSectoriales" : InformeSectorial.objects.all()}
    return render(request, "entidades/InformesSectoriales.html", contexto)

@login_required
def InformesForm(request):
    if request.method == "POST":
        miForm = informesForm(request.POST)
        if miForm.is_valid():
            informes_sector = miForm.cleaned_data.get("sector")
            informes_disponible = miForm.cleaned_data.get("informesDisponibles")
            informes_fecha = miForm.cleaned_data.get("UltimaPublicacion")
            informes = InformeSectorial(sector=informes_sector, informesDisponibles=informes_disponible,UltimaPublicacion=informes_fecha)
            informes.save()
            contexto = {"informesSectoriales" : InformeSectorial.objects.all()}
            return render(request, "entidades/InformesSectoriales.html", contexto)
    else:   
        miForm = informesForm()

    return render(request, "entidades/informesectorial_form.html", {"form" :  miForm}) 

class InformesUpdate(LoginRequiredMixin, UpdateView):
    model = InformeSectorial
    fields = ["sector", "informesDisponibles", "UltimaPublicacion"]
    success_url = reverse_lazy("informesSectoriales")

class InformesDelete(LoginRequiredMixin, DeleteView):
    model = InformeSectorial
    success_url = reverse_lazy("informesSectoriales")



 #_____________Monitor Macro__________



class MonitorList(ListView):
    model = MonitorMacro

class MonitorCreate(LoginRequiredMixin, CreateView):
    model = MonitorMacro
    fields = ["nombre", "mesAnalizado", "fechaPublicacion"]
    success_url = reverse_lazy("monitor")

class MonitorUpdate(LoginRequiredMixin, UpdateView):
    model = MonitorMacro
    fields = ["nombre", "mesAnalizado", "fechaPublicacion"]
    success_url = reverse_lazy("monitor")

class MonitorDelete(LoginRequiredMixin, DeleteView):
    model = MonitorMacro
    success_url = reverse_lazy("monitor")   


#_______Buscar Clientes______

def buscarClientes(request):
    return render(request, "entidades/buscar.html")


def encontrarClientes(request):
    busqueda = request.GET.get("buscar", "")
    clientes = Cliente.objects.filter(nombre__icontains=busqueda)
    contexto = {"Cliente": clientes}
    return render(request, "entidades/clientes.html", contexto)



#_______Login, Logout y Registracion_________

def loginRequest(request):
    if request.method =="POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.jpg"
            finally:
                request.session["avatar"] = avatar
            return render(request, "entidades/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()
    
    return render(request, "entidades/login.html", {"form": miForm})


def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            #usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "entidades/registro.html", {"form": miForm})  


    #_______Edicion de Usuario y Avatar_________

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "entidades/editarperfil.html", {"form": miForm})
    
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "entidades/cambiar_clave.html"
    success_url = reverse_lazy("home")


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #_________ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #__________________________________________
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            #_________ Enviar la imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #____________________________________________________
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "entidades/agregarAvatar.html", {"form": miForm})  

        

  
