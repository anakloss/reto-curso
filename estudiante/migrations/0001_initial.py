# Generated by Django 4.1.7 on 2023-02-18 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Nombre")),
                ("surname", models.CharField(max_length=50, verbose_name="Apellido")),
                ("age", models.PositiveSmallIntegerField(verbose_name="Edad")),
                (
                    "email",
                    models.EmailField(
                        max_length=254, verbose_name="Correo electrónico"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now_add=True, verbose_name="Actualizado"),
                ),
            ],
            options={
                "verbose_name": "Estudiante",
                "verbose_name_plural": "Estudiantes",
            },
        ),
    ]
