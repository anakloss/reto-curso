from django.urls import path
from curso import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("courses/", views.course, name="Cursos"),
    path("courses/addCourse/", views.addCourse),
    path("courses/editCourse/<int:id_course>", views.editCourse),
    path("updateCourse/", views.updateCourse),
    path("courses/deleteCourse/<int:id_course>", views.deleteCourse),

    path("students/", views.student, name="Estudiantes"),
]
