from django.contrib import admin

# Register your models here.
from .models import Category, Course

admin.site.register(Category)
admin.site.register(Course)