from django.db import models

# Create your models here.

class Departamento(models.Model):
    dueno= models.CharField(max_length=50)
    cantHab= models.IntegerField(10)

class Dispositivo(models.Model):
    nombre= models.CharField(max_length=50)
    tipo=models.CharField(max_length=20)
  #  pinGpio=models.IntegerField(10)

class Piso(models.Model):
    nro = models.IntegerField(2)

class habitacion(models.Model):
    dispositivo=models.ForeignKey('Dispositivo', null= True, blank=False, on_delete=models.CASCADE)