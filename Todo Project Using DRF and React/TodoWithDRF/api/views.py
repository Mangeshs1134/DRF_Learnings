from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    def destroy(self, request, *args, **kwargs):
        print('delete')
        return super().destroy(request, *args, **kwargs)