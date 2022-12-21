from rest_framework import serializers
from .models import Student


"""student serializer"""
class Studentserializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length= 20)


    """create function create to post data"""
    def create(self, validation_data):
        return Student.objects.create(**validation_data)

    """create function update to put data"""
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        
        instance.save()
        return instance
