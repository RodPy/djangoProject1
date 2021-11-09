from django.conf import settings

from django.db import models

# Create your models here.

class Departamento(models.Model):
   # dueno= models.CharField(max_length=50)
    dueno= models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=False, on_delete=models.CASCADE)
    cantHab= models.IntegerField(10)

class Dispositivo(models.Model):
    nombre= models.CharField(max_length=50)
    tipo=models.CharField(max_length=20)
    pinGpio=models.PositiveIntegerField(2)

class Piso(models.Model):
    nro = models.IntegerField(2)
    cantDept=models.PositiveIntegerField(2)

class habitacion(models.Model):
    dispositivo=models.ForeignKey('Dispositivo', null= True, blank=False, on_delete=models.CASCADE)