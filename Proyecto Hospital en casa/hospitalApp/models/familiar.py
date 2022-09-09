
from django.db import models
from .usuario import UsuarioModel
from .paciente import PacienteModels

class FamiliarModels(models.Model):
    username = models.ForeignKey(UsuarioModel, on_delete=models.CASCADE)
    paciente = models.ForeignKey(PacienteModels, on_delete=models.CASCADE)
    parentesco = models.CharField(max_length=45)
    correo = models.EmailField(max_length=125)
    
