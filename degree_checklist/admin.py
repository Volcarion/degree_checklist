from django.contrib import admin
from .models import Course, College, Department, Program, ProgramCourse


class CollegeAdmin(admin.ModelAdmin):
    list_display = ('CollegeId', 'Name')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('DepartmententId', 'Name')


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('ProgramId', 'Name')


class ProgramCourseAdmin(admin.ModelAdmin):
    list_display = ('ProgramId', 'CourseId')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('CourseId', 'Name')


# Register your models here.
admin.site.register(College, CollegeAdmin)

admin.site.register(Department, DepartmentAdmin)

admin.site.register(Program, ProgramAdmin)

admin.site.register(ProgramCourse, ProgramCourseAdmin)

admin.site.register(Course, CourseAdmin)
