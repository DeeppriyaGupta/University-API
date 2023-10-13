from rest_framework import serializers
from api.models import University, Program, Student

class UniversitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=University
        fields='__all__'

class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    # many=True
    class Meta:
        model= Program
        fields='__all__'

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
