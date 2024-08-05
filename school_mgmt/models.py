from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    first_name = models.CharField(null=False, max_length=60)
    last_name = models.CharField(null=False, max_length=60)
    year = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])


class Teacher(models.Model):
    first_name = models.CharField(null=False, max_length=60)
    last_name = models.CharField(null=False, max_length=60)
    status = models.CharField(null=True, max_length=60)


class Subject(models.Model):
    name = models.CharField(max_length=60)


class Class(models.Model):
    name = models.CharField(null=False, max_length=60)
    room = models.IntegerField(null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    period = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class StudentClass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_key = models.ForeignKey(Class, on_delete=models.CASCADE)
