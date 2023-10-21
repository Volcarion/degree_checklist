from django.shortcuts import render
# from django.http import HttpResponse
from .models import DegreePlan, Student


def index(request):
    degreePlans = DegreePlan.objects.all()
    students = Student.objects.all()
    return render(request, 'index.html', {'degreePlans': degreePlans,
                                          'students': students})
