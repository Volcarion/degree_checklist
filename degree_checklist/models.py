from django.db import models


class Student(models.Model):
    StudentId = models.IntegerField()
    Name = models.CharField(max_length=250)
    BirthDate = models.DateTimeField()
    Address = models.CharField(max_length=250)


class StudentDegree(models.Model):
    StudentId = models.IntegerField()
    DegreeId = models.IntegerField()


class DegreePlan(models.Model):
    DegreeId = models.IntegerField()
    DegreeName = models.CharField(max_length=250)
    CourseId1 = models.IntegerField()
    CourseId2 = models.IntegerField()


class StudentCourse(models.Model):
    StudentId = models.IntegerField()
    CourseId = models.IntegerField()


class Course(models.Model):
    CourseId = models.IntegerField()
    CourseName = models.CharField(max_length=250)
    PreRequisiteCourseId = models.IntegerField()
