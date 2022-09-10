
from rest_framework import serializers
from hospitalApp.models.usuario import UsuarioModel

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioModel
        fields = '__all__' 
