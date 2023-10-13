from django.shortcuts import render
from rest_framework import viewsets
from api.models import University, Program, Student
from api.serializer import UniversitySerializer, ProgramSerializer, StudentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class UniversityViewSet(viewsets.ModelViewSet):
    queryset=University.objects.all()
    serializer_class=UniversitySerializer

    # http://localhost:8000/api/universities/{universityID}/programs/
    @action(detail=True, methods=['get'])
    def programs(self, request, pk=None):
        try:
            uni=University.objects.get(pk=pk)
            prog=Program.objects.filter(university_ref=uni)
            program_serializer=ProgramSerializer(prog, many=True, context={'request': request})
            return Response(program_serializer.data)
        except Exception as e:
            print(e)
            return Response({'message': 'Current university does not exist, please try another.'})

    # http://localhost:8000/api/universities/{universityID}/students/
    @action(detail=True, methods=['get'])
    def students(self, request, pk=True):
        try:
            get_university=University.objects.get(pk=pk)
            filter_student=Student.objects.filter(university_ref=get_university)
            student_serializer=StudentSerializer(filter_student, many=True, context={'request':request})
            return Response(student_serializer.data)
        except Exception as e:
            print(e)
            return Response({'message': 'Current university does not exist, please try another.' })

class ProgramViewSet(viewsets.ModelViewSet):
    queryset=Program.objects.all()
    serializer_class=ProgramSerializer

    # http://localhost:8000/api/programs/{programsID}/students/
    @action(detail=True, methods=['get'])
    def students(self, request, pk=None):
        try:
            prog=Program.objects.get(pk=pk)
            stu=Student.objects.filter(program_ref=prog)
            student_serializer=StudentSerializer(stu, many=True, context={'request': request})
            return Response(student_serializer.data)
        except Exception as e:
            return Response({'message': 'Current program does not exist, please try another.'})
            

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    # http://localhost:8000/api/universities/{universityID}/programs/{programsID}/students/
    # @action(detail=True, methods=['get'])
    # def students(self, request, pk=None):
    #     try:
    #         uni = University.objects.get(pk=pk)
    #         prog = Program.objects.filter(university_ref=uni).filter(stud)
    #         stud = Student.objects.filter(program_ref__in=prog)  # Use "__in" to filter students for multiple programs
    #         program_serializer = ProgramSerializer(prog, many=True, context={'request': request})
    #         student_serializer = StudentSerializer(stud, many=True, context={'request': request})
    #         response_data = {
    #             'programs': program_serializer.data,
    #             'students': student_serializer.data
    #         }
    #         return Response(response_data)
    #     except University.DoesNotExist:
    #         return Response({'message': 'Current university does not exist, please try another.'})
