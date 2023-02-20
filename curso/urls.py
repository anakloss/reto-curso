from django.urls import path
from curso import views

urlpatterns = [
    path("", views.course, name="Cursos"),
    path("addCourse/", views.addCourse),
    path("editCourse/<int:id_course>", views.editCourse),
    path("updateCourse/", views.updateCourse),
    path("deleteCourse/<int:id_course>", views.deleteCourse),
    path("addStudentsCourse/<int:id_course>", views.addStudents),
    path("addStudentCourse/<int:id_course>", views.addStudentCourse),
]
