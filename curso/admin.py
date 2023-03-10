from django.contrib import admin
from .models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Course, CourseAdmin)
