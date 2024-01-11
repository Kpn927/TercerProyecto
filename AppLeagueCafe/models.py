from django.db import models

# Create your models here.

class Cafe(models.Model):
    nombre = models.CharField(max_length=25)
    
class Users(models.Model):
    Usuario = models.CharField(max_length=25)
    Password = models.CharField(max_length=25)

class delivery(models.Model):
    ubicacion = models.CharField(max_length=25)
    telefono = models.IntegerField()
    Nombre = models.CharField(max_length=25)
    Correo = models.CharField(max_length=25)


