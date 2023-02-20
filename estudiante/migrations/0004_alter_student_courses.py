# Generated by Django 4.1.7 on 2023-02-19 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("curso", "0006_delete_student"),
        ("estudiante", "0003_student_courses"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="courses",
            field=models.ManyToManyField(
                related_name="courses", to="curso.course", verbose_name="Cursos"
            ),
        ),
    ]