from dataclasses import fields

from rest_framework import serializers
from hospitalApp.models import Cargo, Familiar, Pacientes, HistoriaClinica, SignosVitales,TipoIdentificacion, User
from hospitalApp.models import PlantaPersonal

"""Serializador para la tabla users"""
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'

"""Serializador para la tabla Plantapersonal -javier munnos"""
class PlantaPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantaPersonal
        fields = '__all__'


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class TipoIdentificacionSerializer(serializers.ModelSerializer):
    class Metas:
        model = TipoIdentificacion
        fields='__all__'

class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'

class HistoriaClinica(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = '__all__'

class SignosVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignosVitales
        fields = '__all__'

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = '__all__'
