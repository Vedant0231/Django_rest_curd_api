from .serializers import Studentserializer
from .models import Student
from rest_framework.views import APIView
from rest_framework.response import Response

"""
firstly we convert complex data
type into python data type then
convert that python data type into
json form.
"""


"""this curd opration is done by class based method"""
class Studentapi(APIView):

    """function for get data"""
    def get(self, request, id = None, format= None):
        stuid = id
        
        """check that id is there or not"""
        if id is not None:

            stu = Student.objects.get(id = stuid)
            serializers = Studentserializer(stu)

            return Response(serializers.data)

        stu = Student.objects.all()
        serializers = Studentserializer(stu, many=True)    

        return Response(serializers.data)


    """function for insert or post data"""
    def post (self, request, id = None, format = None ):

        serializers = Studentserializer(data=request.data)
        
        if serializers.is_valid():

            serializers.save()

            return Response("data added")

        return Response(serializers.errors)        


    """function for update data"""
    def put (self, request, id= None, format= None):
        studi = id

        if id is not None:

            stu = Student.objects.get(id = studi)
            serializers = Studentserializer(stu, data= request.data, partial=True)

            if serializers.is_valid():

                serializers.save()

            return Response("data updated")

        return Response(serializers.errors) 

        
    """function for delete data"""   
    def delete(self, request, id = None, format= None):
        stuid = id

        if id is not None:

            stu = Student.objects.get(id = stuid)
            stu.delete()

            return Response("data deleted")

        return Response ("sorry can't delete")      