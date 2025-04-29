from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    portada = models.ImageField(upload_to='portadas/')

    def __str__(self):
        return self.titulo