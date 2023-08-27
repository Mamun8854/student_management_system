from django.db import models

# Create your models here.


class Student(models.Model):
    student_name = models.CharField(max_length=100, blank=True, null=True)
    stident_email = models.EmailField(max_length=50, blank=True, null=True)
    student_roll = models.IntegerField(max_length=20, blank=True, null=True)
    student_phone = models.IntegerField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=30, blank=True, null=True)
    semester = models.CharField(max_length=10, blank=True, null=True)
