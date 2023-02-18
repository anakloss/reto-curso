from django.shortcuts import render, redirect
from .models import Course

# Create your views here.

def home(request):
    return render(request, "index.html")

def course(request):
    courses = Course.objects.all()
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
