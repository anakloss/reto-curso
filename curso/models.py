from django.db import models
from estudiante.models import Student

# Create your models here.

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Nombre', max_length=50)
    schedule = models.TimeField(verbose_name='Horario')
    date_init = models.DateField(verbose_name='Fecha inicio')
    date_end = models.DateField(verbose_name='Fecha fin')
    students = models.ManyToManyField(
        Student, verbose_name='Estudiantes', related_name='students')
    created = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Actualizado', auto_now_add=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return f"{self.name} [{self.schedule} Hs.]"