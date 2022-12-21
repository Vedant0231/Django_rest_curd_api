from .serializers import Studentserializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


"""
firstly we convert complex data
type into python data type then
convert that python data type into
json form.
"""


"""this curd opration is done by function based method"""
@api_view(['GET','POST','PUT','DELETE'])
def curd(request, id = None):
    """globally declare variable"""

    stuid = id

    """check type of request method"""
    if request.method == 'GET':
        
        """check id is none or not"""
        if id is not None:

            stu = Student.objects.get(id = stuid)
            serializers = Studentserializer(stu)

            return Response(serializers.data)

        stu = Student.objects.all()
        serializers = Studentserializer(stu, many=True)    

        return Response(serializers.data)


    """check type of request method""" 
    if request.method == 'POST':

        serializers = Studentserializer(data=request.data)
        
        if serializers.is_valid():

            serializers.save()

            return Response("data added")

        return Response(serializers.errors)        


    """check type of request method"""
    if request.method == 'PUT':
        
        """check id is none or not"""
        if id is not None:

            stu = Student.objects.get(id = stuid)
            serializers = Studentserializer(stu, data= request.data, partial=True)

            if serializers.is_valid():

                serializers.save()

            return Response("data updated")

        return Response(serializers.errors) 

        
    """check type of request method"""
    if request.method == 'DELETE':
        
        """check id is none or not"""
        if id is not None:

            stu = Student.objects.get(id = stuid)
            stu.delete()

            return Response("data deleted")

        return Response ("sorry can't delete")       


