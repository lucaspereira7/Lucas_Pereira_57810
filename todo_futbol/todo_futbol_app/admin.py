from django.contrib import admin

# Register your models here.

from .models import *

class Reservar_canchaAdmin(admin.ModelAdmin):
    list_display = ("dia_reserva","hora_reserva","nombre_cancha")

class Buscar_rivalAdmin(admin.ModelAdmin):
    list_display = ("dia_reserva","hora_reserva","nombre_cancha")

class Reservar_eventoAdmin(admin.ModelAdmin):
    list_display = ("dia_reserva","hora_reserva","nombre_cancha")


admin.site.register(Reservar_cancha, Reservar_canchaAdmin)
admin.site.register(Buscar_rival, Buscar_rivalAdmin)
admin.site.register(Reservar_evento, Reservar_eventoAdmin)
