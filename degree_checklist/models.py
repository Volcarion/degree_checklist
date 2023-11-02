from django.db import models


class College(models.Model):
    CollegeId = models.IntegerField()
    Name = models.CharField(max_length=250)


class Department(models.Model):
    DepartmententId = models.IntegerField()
    Name = models.CharField(max_length=250)


class Program(models.Model):
    ProgramId = models.IntegerField()
    Name = models.CharField(max_length=250)


class ProgramCourse(models.Model):
    ProgramId = models.IntegerField()
    CourseId = models.CharField(max_length=250)


class Course(models.Model):
    CourseId = models.CharField(max_length=250)
    Name = models.CharField(max_length=250, default="")
    IsCore = models.CharField(max_length=250)
    IsMajor = models.CharField(max_length=250)
