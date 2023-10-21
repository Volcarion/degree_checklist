from django.contrib import admin
from .models import Course, Student, StudentCourse, StudentDegree, DegreePlan


class DegreePlanAdmin(admin.ModelAdmin):
    list_display = ('DegreeId', 'DegreeName')


class StudentDegreeAdmin(admin.ModelAdmin):
    list_display = ('StudentId', 'DegreeId')


class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('StudentId', 'CourseId')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('StudentId', 'Name', 'Birthdate', 'Address')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('CourseId', 'CourseName')


# Register your models here.
admin.site.register(DegreePlan, DegreePlanAdmin)

admin.site.register(StudentDegree, StudentDegreeAdmin)

admin.site.register(StudentCourse, StudentCourseAdmin)

admin.site.register(Student, StudentAdmin)

admin.site.register(Course, CourseAdmin)
