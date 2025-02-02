from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view 
from .models import StudentModel
from .serializers import StudentSerializer

@api_view(['GET', 'POST'])
def students(request):
    if request.method == 'GET':
        students = StudentModel.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def students_detail(request, pk):
    try:
        student = StudentModel.objects.get(pk=pk)
    except StudentModel.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   
    
