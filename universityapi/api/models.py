from django.db import models
from django.contrib.postgres.fields import ArrayField

class University(models.Model):
    university_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    about=models.TextField()
    type=models.CharField(max_length=60, choices=(('govt', "Government"), ('private', "Private")), default='govt')

    def __str__(self) :
        return self.name
    
# class Program_name(models.Model):
#     name= (('B.Tech', 'B.Tech'), ('BCom', 'BCom'), ('BBA', 'BBA'))

class Program(models.Model):
    program_id=models.AutoField(primary_key=True)
    # name= (('B.Tech', 'B.Tech'), ('BCom', 'BCom'), ('BBA', 'BBA'))
    # prog_name=models.ManyToManyField(Program_name, related_name='programs')
    name=models.CharField(max_length=30, choices=(('BCom', 'BCom'), ('BTech', 'BTech'), ('BBA', 'BBA')))
    # university_ref = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)
    university_ref =models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.name     

class Student(models.Model):
    student_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)
    address=models.CharField(max_length=60)
    program_ref=models.ForeignKey(Program, on_delete=models.CASCADE)
    university_ref =models.ForeignKey(University, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        try:
            if self.program_ref.university_ref != self.university_ref:
                raise ValueError("Program and University mismatch")
        except Program.DoesNotExist:
            return {'message': 'Current university does not exist, please try another.'}
        except University.DoesNotExist:
            return {'message': 'Current university does not exist, please try another.'}
        
        super(Student, self).save(*args, **kwargs)