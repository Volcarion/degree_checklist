from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('courseForm/', views.CourseFormView),
    path('programForm/', views.ProgamFormView),
    path('programCourseForm/', views.ProgramCourseFormView)
]
