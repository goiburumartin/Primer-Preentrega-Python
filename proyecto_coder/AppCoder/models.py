from django.db import models

# Create your models here.
class Seguidores(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Eventos(models.Model):
    nombre= models.CharField(max_length=30)
    integrantes= models.IntegerField()
    tema= models.CharField(max_length=30)
    fechaini=models.DateField()
    fechafin=models.DateField()

class Paginas(models.Model):
    nombre= models.CharField(max_length=30)
    tema= models.CharField(max_length=30)
    integrantes= models.IntegerField()