from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=50)
    surname = models.CharField(verbose_name='Apellido', max_length=50)
    age = models.PositiveSmallIntegerField(verbose_name='Edad')
    # age = models.IntegerField(verbose_name='Edad')
    email = models.EmailField(verbose_name='Correo electrónico')
    # coursos asociados
    created = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Actualizado', auto_now_add=True)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return f"{self.surname}, {self.name}"


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Nombre', max_length=50)
    schedule = models.TimeField(verbose_name='Horario')
    date_init = models.DateField(verbose_name='Fecha inicio')
    date_end = models.DateField(verbose_name='Fecha fin')
    # n° estudiantes asociados
    created = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Actualizado', auto_now_add=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return f"{self.name} [{self.schedule} Hs.]"