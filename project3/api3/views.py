from .models import Student
from .serializers import Studentserializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin


"""This class is create for creating data and get all data"""
class Studentlist(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = Studentserializer


    """function for get all data"""
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    """function for create data"""
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    


"""This class is create for update, delete data and get data by id"""
class Student(GenericAPIView, DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin):
    queryset= Student.objects.all()
    serializer_class = Studentserializer


    """function for update data by id"""
    def put(self ,request, *args,**kwargs):
        return self.update(request, *args, **kwargs)


    """function for get data by id"""
    def get(self ,request, *args,**kwargs):
        return self.retrieve(request, *args, **kwargs)


    """function for delete data by id"""
    def delete(self ,request, *args,**kwargs):
        return self.destroy(request, *args, **kwargs)        
