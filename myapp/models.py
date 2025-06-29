from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    edad = models.IntegerField()
    imagen = models.ImageField(upload_to='imagenes_estudiantes/', blank=True, null=True)

    def __str__(self):
        return self.nombre

