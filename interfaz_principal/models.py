from django.db import models

# Create your models here.
class contacto(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    telefono = models.CharField(max_length=300)
    asunto = models.CharField(max_length=200, null=True)
    mensaje = models.TextField(null=True)

    def __str__(self):
        return self.nombre