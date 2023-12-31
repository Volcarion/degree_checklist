# Generated by Django 4.2.5 on 2023-10-07 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseId', models.IntegerField()),
                ('CourseName', models.CharField(max_length=250)),
                ('PreRequisiteCourseId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DegreePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DegreeId', models.IntegerField()),
                ('DegreeName', models.CharField(max_length=250)),
                ('CourseId1', models.IntegerField()),
                ('CourseId2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentId', models.IntegerField()),
                ('Name', models.CharField(max_length=250)),
                ('BirthDate', models.DateTimeField()),
                ('Address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentId', models.IntegerField()),
                ('CourseId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentDegree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentId', models.IntegerField()),
                ('DegreeId', models.IntegerField()),
            ],
        ),
    ]
