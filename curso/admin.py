from django.contrib import admin
from .models import Student, Course

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)


# VIDEO33