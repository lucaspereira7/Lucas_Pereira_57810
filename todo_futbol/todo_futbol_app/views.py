from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




# botones -------------------------------------------------------------------

def home(request):
    return render(request, "todo_futbol_app/index.html")

@login_required
def sobremi(request):
    return render(request, "todo_futbol_app/sobremi.html")

@login_required
def contacto(request):
    return render(request, "todo_futbol_app/contacto.html")

def mastarde(request):
    return render(request, "todo_futbol_app/mastarde.html")


# modelos -------------------------------------------------------------------

@login_required
def reservaC(request):
    contexto = {"reservaC" : Reservar_cancha.objects.all()}
    return render(request, "todo_futbol_app/reservaC.html" , contexto)

@login_required
def buscarR(request):
    contexto = {"buscarR" : Buscar_rival.objects.all()}
    return render(request, "todo_futbol_app/buscarR.html" , contexto)

@login_required
def reservaE(request):
    contexto = {"reservaE" : Reservar_evento.objects.all()}
    return render(request, "todo_futbol_app/reservaE.html" , contexto)

# formulario buscar -------------------------------------------------------------------

@login_required
def buscarRC(request):
    return render(request, "todo_futbol_app/buscarRC.html")

@login_required
def encontrarRC(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        reservaC = Reservar_cancha.objects.filter(nombre_cancha__icontains=patron)
        contexto = {"reservaC" : reservaC}
    else:
        contexto = {"reservaC" : Reservar_cancha.objects.all()}

    return render(request, "todo_futbol_app/reservaC.html" , contexto)

#_________________________________________

@login_required
def buscarBR(request):
    return render(request, "todo_futbol_app/buscarBR.html")

@login_required
def encontrarBR(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        buscarR = Buscar_rival.objects.filter(nombre_cancha__icontains=patron)
        contexto = {"buscarR" : buscarR}
    else:
        contexto = {"buscarR" : Buscar_rival.objects.all()}

    return render(request, "todo_futbol_app/buscarR.html" , contexto)



#_________________________________________

@login_required
def buscarRE(request):
    return render(request, "todo_futbol_app/buscarRE.html")

@login_required
def encontrarRE(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        reservaE = Reservar_evento.objects.filter(nombre_cancha__icontains=patron)
        contexto = {"reservaE" : reservaE}
    else:
        contexto = {"reservaE" : Reservar_evento.objects.all()}

    return render(request, "todo_futbol_app/reservaE.html" , contexto,)


#_________________________________________

@login_required
def buscarVC(request):
    return render(request, "todo_futbol_app/buscarVC.html")

@login_required
def encontrarVC(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        vendercomprar = VenderComprar.objects.filter(nombre_articulo__icontains=patron)
        contexto = {"vendercomprar" : vendercomprar}
    else:
        contexto = {"vendercomprar" : VenderComprar.objects.all()}

    return render(request, "todo_futbol_app/vendercomprar.html" , contexto,)


# CBV -------------------------------------------------------------------

#____________________reservaC_____________________


class reservaCList (LoginRequiredMixin, ListView):
    model = Reservar_cancha
    context_object_name = 'reservaC'

class reservaCCreate (LoginRequiredMixin, CreateView):
    model = Reservar_cancha
    fields = ["nombre_cancha" , "hora_reserva" , "dia_reserva"]
    success_url = reverse_lazy("reservaC")

class reservaCUpdate (LoginRequiredMixin, UpdateView):
    model = Reservar_cancha
    fields = ["nombre_cancha" , "hora_reserva" , "dia_reserva"]
    success_url = reverse_lazy("reservaC")

class reservaCDelete (LoginRequiredMixin, DeleteView):
    model = Reservar_cancha
    success_url = reverse_lazy("reservaC")

#____________________buscarR_____________________
class buscarRList (LoginRequiredMixin, ListView):
    model = Buscar_rival
    context_object_name = 'buscarR'

class buscarRCreate (LoginRequiredMixin, CreateView):
    model = Buscar_rival
    fields = ["nombre_cancha" , "hora_reserva" , "dia_reserva" , "tu_equipo"]
    success_url = reverse_lazy("buscarR")

class buscarRUpdate (LoginRequiredMixin, UpdateView):
    model = Buscar_rival
    fields = ["nombre_cancha" , "hora_reserva" , "dia_reserva" , "tu_equipo"]
    success_url = reverse_lazy("buscarR")

class buscarRDelete (LoginRequiredMixin, DeleteView):
    model = Buscar_rival
    success_url = reverse_lazy("buscarR")

#____________________reservaE_____________________
class reservaEList (LoginRequiredMixin, ListView):
    model = Reservar_evento
    context_object_name = 'reservaE'

class reservaECreate (LoginRequiredMixin, CreateView):
    model = Reservar_evento
    fields = ["nombre_cancha" , "hora_reserva" , "dia_reserva" , "cantidad_horas" , "tipo_evento"]
    success_url = reverse_lazy("reservaE")

class reservaEUpdate (LoginRequiredMixin, UpdateView):
    model = Reservar_evento
    fields = ["nombre_cancha" , "hora_reserva" , "dia_reserva" , "cantidad_horas" , "tipo_evento"]
    success_url = reverse_lazy("reservaE")

class reservaEDelete (LoginRequiredMixin, DeleteView):
    model = Reservar_evento
    success_url = reverse_lazy("reservaE")

#____________________vendercomprar_____________________
class vendercomprarList (LoginRequiredMixin, ListView):
    model = VenderComprar
    context_object_name = 'vendercomprar'

class vendercomprarCreate (LoginRequiredMixin, CreateView):
    model = VenderComprar
    fields = ["nombre_articulo" , "estado_articulo" , "talle" , "precio" , "numero_celular"]
    success_url = reverse_lazy("vendercomprar")

class vendercomprarUpdate (LoginRequiredMixin, UpdateView):
    model = VenderComprar
    fields = ["nombre_articulo" , "estado_articulo" , "talle" , "precio" , "numero_celular"]
    success_url = reverse_lazy("vendercomprar")

class vendercomprarDelete (LoginRequiredMixin, DeleteView):
    model = VenderComprar
    success_url = reverse_lazy("vendercomprar")


# login / logout / registracion -------------------------------------------------------------------
    
def loginRequest (request):
    if request.method == "POST":
        usuario = request.POST ["username"]
        clave = request.POST ["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.jpg"
            finally:
                request.session["avatar"] = avatar

            return render (request, "todo_futbol_app/index.html")
        
        else:
            return redirect (reverse_lazy('login'))

    else:
        miForm = AuthenticationForm()
    
    return render (request, "todo_futbol_app/login.html", {"form" : miForm})

def Registro (request):
    if request.method == "POST":
        miForm = RegistroForms(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForms()

    return render(request, "todo_futbol_app/registro.html", {"form":miForm})


# Edicion de perfil -------------------------------------------------------------------

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username = usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "todo_futbol_app/profile.html", {"form": miForm})
    

class EditarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = "todo_futbol_app/password.html"
    success_url = reverse_lazy ("home")


# Avatar -------------------------------------------------------------------

@login_required
def agregar_avatar (request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username = request.user)
            imagen = miForm.cleaned_data["imagen"]
            Bavatar = Avatar.objects.filter(user=usuario)
            if len(Bavatar) > 0:
                for i in range(len(Bavatar)):
                    Bavatar[i].delete()  
            avatar = Avatar (user=usuario, imagen=imagen)
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            return redirect(reverse_lazy("home"))
    
    else:
        miForm = AvatarForm()
    return render(request, "todo_futbol_app/avatar.html", {"form": miForm})
    
