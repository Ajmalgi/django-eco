from django.shortcuts import render
from .serializers import StudentSerializers
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from . models import Students
import json
# Create your views here.

@api_view(['POST'])
def add_student(request):
    try:
        params = request.data
        serialized_data = StudentSerializers(data=params)  
        
        if serialized_data.is_valid():
            serialized_data.save()
            status_code = 201
            msg = 'student added'
        else: 
            status_code = 403 
            msg = 'form error'

    except:
        status_code = 500 
        msg = 'somthing went wrong'
    
    return Response({'msg':msg,'status':status_code})

@api_view(['GET'])
def view_student(request):
    students = Students.objects.all()
    serialized_data = StudentSerializers(students, many=True)
    return Response({'student_list':serialized_data.data})


@api_view(['DELETE'])
def delete_student(request,sid):
    try:
        students = Students.objects.get(id=sid)
        students.delete()
        msg = 'student deleted'
    
    except:
        msg = 'student not found'
    
    return Response({'msg':msg})

@api_view(['PUT'])
def update_student(request,sid):
    params = request.data
    try:

     student = Students.objects.get(id = sid)
     serialized_data = StudentSerializers(student,data=params)
     if serialized_data.is_valid():
        serialized_data.save()
        msg = 'updated'
    except:
        msg = 'not updated'



