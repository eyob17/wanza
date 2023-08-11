from pickle import TRUE
from django.db import models

# Create your models here.
# models.py
from django.contrib.auth.models import User
from django.db import models
from tomlkit import boolean



class Student(models.Model):
    user = models.OneToOneField(
    User, 
    on_delete=models.SET_NULL, 
    null=True,
    default=None
)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50 , unique=TRUE , default='Undeclared')
    email = models.EmailField(max_length=254)
    course_type = models.CharField(max_length=100,blank=True, null=True)
    password = models.CharField(max_length=10)
    batch = models.CharField(max_length=254,blank=True, null=True)
    active = models.BooleanField(default='False')
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
 
 
from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.TextField() 
    credit_hours = models.IntegerField()
    course_image = models.ImageField(upload_to='course_images/')
    course_type = models.CharField(max_length=100)
    course_files = models.ManyToManyField('CourseFile', related_name='courses')
 
    
    def __str__(self):
        return self.course_name
    
class CourseFile(models.Model):
    file = models.FileField(upload_to='course_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.file.name    
class Services(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.TextField() 
    service_image = models.ImageField(upload_to='course_images/')
    Service_type = models.CharField(max_length=100)
    
    def __str__(self):
        return self.service_name