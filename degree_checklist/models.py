from django.db import models


class College(models.Model):
    CollegeId = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=250)


class Department(models.Model):
    DepartmententId = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=250)
    CollegeId = models.IntegerField(default=0)


class Program(models.Model):
    ProgramId = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=250)
    DepartmententId = models.IntegerField(default=0)


class ProgramCourse(models.Model):
    ProgramId = models.IntegerField()
    CourseId = models.CharField(max_length=250)


class Course(models.Model):
    CourseId = models.CharField(max_length=250, primary_key=True)
    Name = models.CharField(max_length=250, default="")
    IsCore = models.CharField(max_length=250)
    IsMajor = models.CharField(max_length=250)
