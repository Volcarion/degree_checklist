from django.shortcuts import render
from django.contrib import messages
# from django.http import HttpResponse
from .models import Course, College, Department, Program, ProgramCourse
from .forms import CourseForm, ProgramForm, ProgramCourseForm


def index(request):
    programs = Program.objects.all()
    courses = Course.objects.all()
    return render(request, 'index.html', {'programs': programs,
                                          'courses': courses})


def CourseFormView(request):
    courseForm = CourseForm(request.POST, request.FILES)
    if courseForm.is_valid():
        courseForm.save()

    return render(request, 'courseForm.html', {'courseForm': courseForm})


def ProgamFormView(request):
    programForm = ProgramForm(request.POST, request.FILES)
    if programForm.is_valid():
        programForm.save()

    return render(request, 'programForm.html', {'programForm': programForm})


def ProgramCourseFormView(request):
    programCourseForm = ProgramCourseForm(request.POST, request.FILES)
    if programCourseForm.is_valid():
        programCourseForm.save()

    return render(request, 'programCourseForm.html', {'programCourseForm': programCourseForm})
