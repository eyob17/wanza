from django.contrib import admin

# Register your models here.
# students/admin.py

from django.contrib import admin
from .models import Course, Services, Student

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Services)
