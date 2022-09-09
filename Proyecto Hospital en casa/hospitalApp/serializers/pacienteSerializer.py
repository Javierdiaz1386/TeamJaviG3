
from rest_framework import serializers
from models.paciente import PacienteModels

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacienteModels
        fields = '__all__' 
