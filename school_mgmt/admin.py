from django.contrib import admin
from .models import Subject, Teacher, Student, Class


admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Class)
