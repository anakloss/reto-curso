from django.urls import path
from estudiante import views

urlpatterns = [
    path("", views.student, name="Estudiantes"),
    path("addStudent/", views.addStudent),
    path("editStudent/<int:id_student>", views.editStudent),
    path("updateStudent/", views.updateStudent),
    path("deleteStudent/<int:id_student>", views.deleteStudent),
]
