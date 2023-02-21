from django.shortcuts import render, redirect
from django.db.models import Count
from estudiante.models import Student
from .models import Course
from datetime import datetime, timedelta


# Create your views here.

def home(request):
    # Filter top 3
    period = datetime.now() - timedelta(days=180)
    courses = Course.objects.annotate(s_count=Count('students')).order_by('-s_count').filter(
        updated__gte=period)
    return render(request, "index.html", {'courses': courses[:3]})


def course(request):
    courses = Course.objects.all().order_by('name')
    return render(request, "courses.html", {'courses': courses})


def addCourse(request):
    name = request.POST['txtName']
    schedule = request.POST['timeSchedule']
    date_init = request.POST['dateInit']
    date_end = request.POST['dateEnd']

    course = Course.objects.create(
        name=name, schedule=schedule, date_init=date_init, date_end=date_end)
    return redirect('/courses')

def editCourse(request, id_course):
    course = Course.objects.get(id=id_course)
    return render(request, 'course-details.html', {'course': course})


def updateCourse(request):
    id = request.POST['txtId']
    name = request.POST['txtName']
    schedule = request.POST['timeSchedule']
    date_init = request.POST['dateInit']
    date_end = request.POST['dateEnd']
    
    course = Course.objects.get(id=id)
    course.name = name
    course.schedule = schedule
    course.date_init = date_init
    course.date_end = date_end
    course.save()
    return redirect('/courses')


def deleteCourse(request, id_course):
    course = Course.objects.get(id=id_course)
    course.delete()
    return redirect('/courses')


def addStudents(request, id_course):
    # List students of the course
    course = Course.objects.get(id=id_course)
    students = Student.objects.all().order_by('surname')
    return render(request, 'course-student.html', {'course': course, 'students': students})


def addStudentCourse(request, id_course):
    student = request.POST['newStudent']
    course = Course.objects.get(id=id_course)
    course.students.add(student)
    course.updated = datetime.now()
    course.save()
    return redirect('/courses/addStudentsCourse/' + str(id_course))