from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def student_api(request):
    # read - commands
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            # return JsonResponse(serializer)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    # create - commands
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : "data got created"}
            json_data = JSONRenderer().render(res.get('msg'))
            return HttpResponse(json_data, content_type="application/json")
        return JsonResponse(serializer.errors)
    

    # update --commands
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        update_student = Student.objects.get(id=id)
        serializer = StudentSerializer(update_student, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : "data got updated"}
            json_data = JSONRenderer().render(res.get('msg'))
            return HttpResponse(json_data, content_type="application/json")
        return JsonResponse(serializer.errors)


    # delete commands
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {'msg' : "data got deleted"}
        json_data = JSONRenderer().render(res.get('msg'))
        return HttpResponse(json_data, content_type="application/json")
