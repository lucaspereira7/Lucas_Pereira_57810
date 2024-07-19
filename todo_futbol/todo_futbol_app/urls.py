from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    # botones
    path('', home, name = "home"),
    path('contacto/', contacto, name = "contacto"),
    path('sobremi/', sobremi, name = "sobremi"),
    path('mastarde/', mastarde, name = "mastarde"),


    # buscar
    path('buscarRC/', buscarRC, name = "buscarRC"),
    path('encontrarRC/', encontrarRC, name = "encontrarRC"),
    #---------
    path('buscarBR/', buscarBR, name = "buscarBR"),
    path('encontrarBR/', encontrarBR, name = "encontrarBR"),
    #---------
    path('buscarRE/', buscarRE, name = "buscarRE"),
    path('encontrarRE/', encontrarRE, name = "encontrarRE"),
    #---------
    path('buscarVC/', buscarVC, name = "buscarVC"),
    path('encontrarVC/', encontrarVC, name = "encontrarVC"),
    

    # List
    path('reservaC/', reservaCList.as_view(), name = "reservaC"),
    path('buscarR/', buscarRList.as_view(), name = "buscarR"),
    path('reservaE/', reservaEList.as_view(), name = "reservaE"),
    path('vendercomprar/', vendercomprarList.as_view(), name = "vendercomprar"),

    # Create
    path('reservaCCreate/', reservaCCreate.as_view(), name = "reservaCCreate"),
    path('buscarRCreate/', buscarRCreate.as_view(), name = "buscarRCreate"),
    path('reservaECreate/', reservaECreate.as_view(), name = "reservaECreate"),
    path('vendercomprarCreate/', vendercomprarCreate.as_view(), name = "vendercomprarCreate"),

    # Update
    path('reservaCUpdate/<int:pk>/', reservaCUpdate.as_view(), name = "reservaCUpdate"),
    path('buscarRUpdate/<int:pk>/', buscarRUpdate.as_view(), name = "buscarRUpdate"),
    path('reservaEUpdate/<int:pk>/', reservaEUpdate.as_view(), name = "reservaEUpdate"),
    path('vendercomprarUpdate/<int:pk>/', vendercomprarUpdate.as_view(), name = "vendercomprarUpdate"),

    # Delete
    path('reservaCDelete/<int:pk>/', reservaCDelete.as_view(), name = "reservaCDelete"),
    path('buscarRDelete/<int:pk>/', buscarRDelete.as_view(), name = "buscarRDelete"),
    path('reservaEDelete/<int:pk>/', reservaEDelete.as_view(), name = "reservaEDelete"),
    path('vendercomprarDelete/<int:pk>/', vendercomprarDelete.as_view(), name = "vendercomprarDelete"),

    # Login / Logout / Registracion
    path('login/', loginRequest, name = "login"),
    path('logout/', LogoutView.as_view(template_name="todo_futbol_app/logout.html"), name="logout"),
    path('registro/', Registro, name="registro"),

    # EditProfile 
    path('profile/', editProfile, name = "profile"),
    path('<int:pk>/password/', EditarPassword.as_view() , name = "password"),

    # Avatar
    path('agregar_avatar/', agregar_avatar , name = "agregar_avatar"),

]

