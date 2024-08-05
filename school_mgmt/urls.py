from django.urls import path

from .views import index, view, add_student, add_teacher, add_class

urlpatterns = [
    path("", index, name="index"),
    path("view", view, name="view"),
    path("addstudent", add_student, name="add_student"),
    path("addteacher", add_teacher, name="add_teacher"),
    path("addclass", add_class, name="add_class"),
]
