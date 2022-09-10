
from django.db import models
from .usuario import UsuarioModel

class PsaludModels(models.Model):
    username = models.ForeignKey(UsuarioModel, on_delete=models.CASCADE)
    rol = models.CharField(max_length=45)
    especialidad = models.CharField(max_length=45)
    def __str__(self):
        return self.rol
    


    