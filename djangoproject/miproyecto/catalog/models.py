from django.db import models

# Create your models here.


class Director(models.Model):
    name=models.CharField(max_length=64, help_text="Nombre del Director")
    apellido=models.CharField(max_length=64, help_text="Apellido del Director")
    nacimiento=models.DateField(help_text="Fecha de nacimiento")

    
    def __str__(self):
        return self.apellido

class Genre(models.Model):
    name=models.CharField(max_length=64, help_text="Nombre del genero")

    def __str__(self):
        return self.name

class Pelicula(models.Model):
    name=models.CharField(max_length=64, help_text="Nombre de la pelicula")
    anio=models.DateField(help_text="Fecha de estreno")
    director=models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    descripcion=models.TextField(max_length=255, help_text="Sinopsis de la pelicula")
    genero=models.ManyToManyField(Genre)

    def __str__(self):
        return self.name


