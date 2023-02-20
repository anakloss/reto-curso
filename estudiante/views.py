from django.shortcuts import render, redirect
from .models import Student

# Create your views here.


def student(request):
    students = Student.objects.all()
    return render(request, "students.html", {'students': students})

def addStudent(request):
    name = request.POST['txtName']
    surname = request.POST['txtSurname']
    age = request.POST['intAge']
    email = request.POST['email']

    student = Student.objects.create(
        name=name, surname=surname, age=age, email=email)
    return redirect('/students')

def editStudent(request, id_student):
    student = Student.objects.get(id=id_student)
    return render(request, 'student-details.html', {'student': student})


def updateStudent(request):
    id = request.POST['txtId']
    name = request.POST['txtName']
    surname = request.POST['txtSurname']
    age = request.POST['intAge']
    email = request.POST['email']


    student = Student.objects.get(id=id)
    student.name = name
    student.surname = surname
    student.age = age
    student.email = email
    student.save()

    return redirect('/students')


def deleteStudent(request, id_student):
    student = Student.objects.get(id=id_student)
    student.delete()
    return redirect('/students')

def listCourses(request, id_student):
    student = Student.objects.get(id=id_student)
    print(student.students.all())
    return render(request, "student-courses.html", {'student': student, 'courses': student.students.all()})
