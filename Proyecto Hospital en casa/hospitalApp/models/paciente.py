
from django.db import models
from .Psalud import PsaludModels
from .usuario import UsuarioModel

class PacienteModels(models.Model):
    id_psalud = models.ForeignKey(PsaludModels, on_delete=models.CASCADE)
    username = models.ForeignKey(UsuarioModel, on_delete=models.CASCADE, null=True)
    direccion = models.CharField(max_length=45)
    ciudad = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField(auto_now=False,auto_now_add=False)
    