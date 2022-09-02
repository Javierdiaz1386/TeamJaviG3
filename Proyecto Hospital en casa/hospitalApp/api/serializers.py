from dataclasses import fields
from rest_framework import serializers
from hospitalApp.models import User

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'

