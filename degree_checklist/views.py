from django.shortcuts import render
# from django.http import HttpResponse
from .models import Program, Course


def index(request):
    programs = Program.objects.all()
    courses = Course.objects.all()
    return render(request, 'index.html', {'programs': programs,
                                          'courses': courses})
