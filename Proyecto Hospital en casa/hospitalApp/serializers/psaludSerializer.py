
from rest_framework import serializers
from models.Psalud import PsaludModels

class PsaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = PsaludModels
        fields = '__all__' 
