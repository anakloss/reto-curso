from django.urls import path
from estudiante import views

urlpatterns = [
    path("students/", views.student, name="Estudiantes"),
    path("students/addStudent/", views.addStudent),
    path("students/editStudent/<int:id_student>", views.editStudent),
    path("updateStudent/", views.updateStudent),
    path("students/deleteStudent/<int:id_student>", views.deleteStudent),
]
