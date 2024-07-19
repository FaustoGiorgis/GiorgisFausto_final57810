from django.urls import path, include
from entidades.views import *
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', home, name="home"),
    
    
   
    path('quienesSomos', quienesSomos, name="quienesSomos"),
 
    
    
    path('buscarClientes', buscarClientes, name="buscarClientes"),
    path('encontrarClientes', encontrarClientes, name="encontrarClientes"),


    #______Cliente
    path('clientes', clientes, name="clientes"),
    path('clienteForm', clientesForm, name="clienteForm"),
    path('clienteUpdate/<id_cliente>/', clienteUpdate, name="clienteUpdate"),
    path('clienteDelete/<id_cliente>/', clienteDelete, name="clienteDelete"),

    #______Informes Sectoriales
    path('informesSectoriales/', InformesSectoriales, name="informesSectoriales"),
    path('informesectorial_form', InformesForm, name="informesSectorialesForm"),
    path('informesUpdate/<int:pk>', InformesUpdate.as_view(), name="informesUpdate"),
    path('informesDelete/<int:pk>/', InformesDelete.as_view(), name="informesDelete"), 

    #______Prensa
    path('prensa', prensa, name="prensa"),
    path('prensa_form', PrensaForm, name="prensaForm"),
    path('prensaUpdate/<int:pk>', prensaUpdate.as_view(), name="prensaUpdate"),
    path('prensaDelete/<int:pk>/', prensaDelete.as_view(), name="prensaDelete"), 

    #_____Monitor

    path('monitormacro_list/', MonitorList.as_view(), name="monitor"),    
    path('monitorCreate/', MonitorCreate.as_view(), name="monitorCreate"), 
    path('monitorUpdate/<int:pk>/', MonitorUpdate.as_view(), name="monitorUpdate"), 
    path('monitorDelete/<int:pk>/', MonitorDelete.as_view(), name="monitorDelete"), 

    #______Login, Logout y Registracion

    path('login', loginRequest, name="login"),  
    path('logout/', LogoutView.as_view(template_name="entidades/logout.html"), name="logout"),
    path('registro/', register, name="registro"),


    #___ Edición de Perfil / Avatar
    path('perfil', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),




    
    ]


