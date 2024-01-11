from django.db import models

# Create your models here.
class heroe(models.Model):

    nombre = models.CharField(max_length=40)
    habilidad = models.CharField(max_length=70)
    raza = models.CharField(max_length=40)
    vehiculo = models.CharField(max_length=40)

class villano(models.Model):
    nombre = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    vehiculo = models.CharField(max_length=100)

class vehiculo(models.Model):
    modelo = models.CharField(max_length= 40)
    propietario = models.CharField(max_length= 40)

    