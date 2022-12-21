from django.db import models


"""model for student data"""
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length= 20)