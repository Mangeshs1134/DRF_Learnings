from rest_framework import viewsets
from .models import TeamPlayer
from .serializers import TeamPlayerSerialzier


# Create your views here.

class TeamPlayerViewSet(viewsets.ModelViewSet):
    queryset = TeamPlayer.objects.all()
    serializer_class = TeamPlayerSerialzier
