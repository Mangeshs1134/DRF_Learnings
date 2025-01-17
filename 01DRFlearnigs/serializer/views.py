from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse, JsonResponse

# Create your views here.
# single student data

def student_detail(request, roll):
    current_student = Student.objects.get(roll_no = roll) 
    serializer = StudentSerializer(current_student)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    # json response safe = true


# all student data

def student_list(request):
    current_student = Student.objects.all() 
    serializer = StudentSerializer(current_student, many= True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)
