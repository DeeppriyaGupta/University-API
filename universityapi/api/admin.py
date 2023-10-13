from django.contrib import admin
from api.models import University, Program, Student
# Register your models here.

class UniversityAdmin(admin.ModelAdmin):
    list_display=('university_id','name', 'location', 'about', 'type')
    search_fields=('name',)
    
class ProgramAdmin(admin.ModelAdmin):
    list_display=('program_id','name', 'university_ref')

class StudentAdmin(admin.ModelAdmin):
    list_display=('student_id','name', 'address', 'program_ref','university_ref')
    list_filter=('university_ref', 'program_ref')

admin.site.register(University, UniversityAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Student, StudentAdmin)

#username=cherry
#email=cherry@gmail.com
#password=123456