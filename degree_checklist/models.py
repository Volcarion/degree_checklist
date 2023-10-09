from django.db import models


class Student(models.Model):
    StudentId = models.CharField(max_length=250)
    Name = models.CharField(max_length=250)
    BirthDate = models.DateTimeField()
    Address = models.CharField(max_length=250)


class StudentDegree(models.Model):
    StudentId = models.CharField(max_length=250)
    DegreeId = models.IntegerField()


class DegreePlan(models.Model):
    DegreeId = models.IntegerField()
    DegreeName = models.CharField(max_length=250)
    CourseId1 = models.CharField(max_length=250)
    CourseId2 = models.CharField(max_length=250)


class StudentCourse(models.Model):
    StudentId = models.CharField(max_length=250)
    CourseId = models.CharField(max_length=250)


class Course(models.Model):
    CourseId = models.CharField(max_length=250)
    CourseName = models.CharField(max_length=250)
    PreRequisiteCourseId = models.CharField(max_length=250)
