from django.contrib import admin
from Assignment2.degree_checklist.models import Course, Student, StudentCourse, StudentDegree, DegreePlan

# Register your models here.
admin.site.register(Student, Course, StudentCourse, StudentDegree, DegreePlan)