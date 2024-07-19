from django.db import models
from django.contrib.auth.models import User

# Modelos de mi aplicacion

# ------------------------------------------------------
class Reservar_cancha(models.Model):
    nombre_cancha = models.CharField(max_length=20)
    hora_reserva = models.CharField(max_length=20)
    dia_reserva = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Reserva de cancha"
        verbose_name_plural = "Reservas de cancha"
        ordering = ["dia_reserva","hora_reserva"]

    def __str__(self):
        return f"{self.nombre_cancha}"
    


# ------------------------------------------------------
class Buscar_rival(models.Model):
    nombre_cancha = models.CharField(max_length=20)
    hora_reserva = models.CharField(max_length=20)
    dia_reserva = models.CharField(max_length=20)
    tu_equipo = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Buscando rival"
        verbose_name_plural = "Buscandores de rival"
        ordering = ["dia_reserva","hora_reserva"]

    def __str__(self):
        return f"{self.tu_equipo}"


# ------------------------------------------------------
class Reservar_evento(models.Model):
    nombre_cancha = models.CharField(max_length=20)
    hora_reserva = models.CharField(max_length=20)
    dia_reserva = models.CharField(max_length=20)
    cantidad_horas = models.IntegerField()
    tipo_evento = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Reserva de evento"
        verbose_name_plural = "Reservas de evento"
        ordering = ["dia_reserva","hora_reserva"]

    def __str__(self):
        return f"{self.nombre_cancha}, {self.dia_reserva}"
    
# ------------------------------------------------------
class VenderComprar(models.Model):
    nombre_articulo = models.CharField(max_length=40)
    estado_articulo = models.CharField(max_length=10)
    talle = models.CharField(max_length=10)
    precio = models.IntegerField()
    numero_celular = models.IntegerField()

    class Meta:
        verbose_name = "vender/comprar"
        verbose_name_plural = "vender/comprar"
        ordering = ["talle","precio"]

    def __str__(self):
        return f"{self.nombre_articulo}, {self.talle}, {self.estado_articulo}"
    
# ------------------------------------------------------
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey (User, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.user}, {self.imagen}"
        
        
