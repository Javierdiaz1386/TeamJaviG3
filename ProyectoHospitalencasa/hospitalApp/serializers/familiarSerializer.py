
from rest_framework import serializers
from hospitalApp.models.familiar import FamiliarModels

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamiliarModels
        fields = '__all__' 
