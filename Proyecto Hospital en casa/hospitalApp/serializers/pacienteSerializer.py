
from rest_framework import serializers
from hospitalApp.models.paciente import PacienteModels

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacienteModels
        fields = '__all__' 
