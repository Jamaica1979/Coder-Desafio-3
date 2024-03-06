from django.db import models


# Create your models here.

class Usuario (models.Model):
      
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField() 
    edad = models.IntegerField()

    def __str__(self):

        return f'Don {self.apellido} se ha registrado con éxito'


class Ingreso(models.Model):
     
    fecha= models.DateField()
    importe= models.IntegerField()
    categoria = models.CharField(max_length=60)
    descripcion= models.CharField(max_length=60)

    def __str__(self):
        return 'Se ha contabilizado con éxito'


class Egreso(models.Model):
    
    fecha= models.DateField()
    importe= models.IntegerField()
    categoria = models.CharField(max_length=60)
    descripcion= models.CharField(max_length=60)

    def __str__(self):
        return 'Se ha contabilizado con éxito'

