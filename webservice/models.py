from django.db import models

# Create your models here.

class usuarios(models.Model):
    password = models.CharField(max_length=60)

class partidas(models.Model):
    fecha = models.CharField(max_length=60)
    id_usuario = models.ForeignKey(usuarios, related_name="id_usuario", on_delete=models.CASCADE)
    minutos_jugados= models.IntegerField()
    puntaje=models.IntegerField()