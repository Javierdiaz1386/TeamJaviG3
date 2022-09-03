from django.contrib import admin
from hospitalApp import models

admin.site.register(models.User)
admin.site.register(models.TipoIdentificacion)
admin.site.register(models.PlantaPersonal)
admin.site.register(models.Cargo)
admin.site.register(models.Pacientes)
admin.site.register(models.HistoriaClinica)
admin.site.register(models.SignosVitales)
admin.site.register(models.Familiar)


