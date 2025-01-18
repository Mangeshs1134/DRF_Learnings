from rest_framework import serializers
from .models import MatchLive

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchLive
        fields = ['team1', 'team2', 'inning']