from rest_framework import serializers
from .models import TeamPlayer

class TeamPlayerSerialzier(serializers.ModelSerializer):
    class Meta :
        model = TeamPlayer
        fields = ['name', 'age', 'runs', 'balls'] 