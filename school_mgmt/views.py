# TODO:
#   add success/failure message after post?
#   form validation front/backend
#

from django.shortcuts import render
from .models import Student, Teacher, Class, Subject
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def view(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    classes = Class.objects.all()
    context = {
        'student_list': students,
        'teacher_list': teachers,
        'class_list': classes,
    }
    return render(request, "view.html", context)


def add_student(request):
    if request.method == "GET":
        return render(request, "addstudent.html")

    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    year = request.POST.get('year')
    # print(first_name, last_name, year)
    Student.objects.create(first_name=first_name, last_name=last_name, year=year)
    context = {'message': "Successfully added student!"}
    return render(request, "addstudent.html", context)


def add_teacher(request):
    if request.method == "GET":
        return render(request, "addteacher.html")

    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    status = request.POST.get('status')
    # print(first_name, last_name, status)
    Teacher.objects.create(first_name=first_name, last_name=last_name, status=status)
    context = {'message': "Successfully added teacher!"}
    return render(request, "addteacher.html", context)


def add_class(request):
    if request.method == "GET":
        teachers = Teacher.objects.all()
        subjects = Subject.objects.all()

        context = {
            "teachers": teachers,
            "subjects": subjects,
        }
        return render(request, "addclass.html", context)

    name = request.POST.get('name')
    room = request.POST.get('room')
    subject = Subject.objects.get(id=request.POST.get('subject'))
    period = request.POST.get('period')
    teacher = Teacher.objects.get(id=request.POST.get('teacher'))
    # print(name, room, subject, period, teacher)
    Class.objects.create(name=name, room=room, subject=subject, period=period, teacher=teacher)

    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    context = {
        "teachers": teachers,
        "subjects": subjects,
        'message': "Successfully added class!",
    }
    return render(request, "addclass.html", context)
