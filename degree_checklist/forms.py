from django import forms
from .models import Course, College, Department, Program, ProgramCourse


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = "__all__"


class ProgramCourseForm(forms.ModelForm):
    class Meta:
        model = ProgramCourse
        fields = "__all__"
