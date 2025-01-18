from rest_framework import generics 
from .serializers import MatchSerializer
from .models import MatchLive

# Create your views here.

class MatchLiveList(generics.ListCreateAPIView):
    queryset = MatchLive.objects.all()
    serializer_class = MatchSerializer

class MatchLiveDetail(generics.RetrieveAPIView):
    queryset = MatchLive.objects.all()
    serializer_class = MatchSerializer

class MatchLiveCreate(generics.CreateAPIView):
    queryset = MatchLive.objects.all()
    serializer_class = MatchSerializer

class MatchLiveUpdate(generics.UpdateAPIView):
    queryset = MatchLive.objects.all()
    serializer_class = MatchSerializer

class MatchLiveDelete(generics.DestroyAPIView):
    queryset = MatchLive.objects.all()
    serializer_class = MatchSerializer

