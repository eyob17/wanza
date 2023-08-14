

from ast import Global
from gzip import FNAME
from pickle import TRUE
from profile import Profile
import select
from ssl import AlertDescription
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# views.py
from django.contrib.auth.decorators import user_passes_test
from students.models import Student , Services
# views.py

def is_staff_user(user):
    return user.is_staff

@user_passes_test(is_staff_user)
def students_detail(request):
    # Retrieve all users
    all_users = Student.objects.all()
    return render(request, 'auth/students_detail.html', {'users': all_users})
@user_passes_test(is_staff_user)
def admin_courses(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course_file_id = request.POST.get('course_file_id')
        new_uploaded_file = request.FILES.get('new_course_file')
        uploaded_file = request.FILES.get('course_file')
        if course_name and course_file_id and new_uploaded_file:
            try:
                course = Course.objects.get(course_name=course_name)
                course_file = CourseFile.objects.get(id=course_file_id)
                course_file.file = new_uploaded_file
                course_file.save()
            except (Course.DoesNotExist, CourseFile.DoesNotExist):
                pass
        if course_name and uploaded_file:
              try:
                  course = Course.objects.get(course_name=course_name)
                  course_file = CourseFile.objects.create(file=uploaded_file)
                  course.course_files.add(course_file)
              except Course.DoesNotExist:
                  pass
      
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'auth/admin_courses.html', context)


# def admin_courses(request):
#     if request.method == 'POST':
#         course_name = request.POST.get('course_name')
#         uploaded_file = request.FILES.get('course_file')

#         if course_name and uploaded_file:
#             try:
#                 course = Course.objects.get(course_name=course_name)
#                 course_file = CourseFile.objects.create(file=uploaded_file)
#                 course.course_files.add(course_file)
#             except Course.DoesNotExist:
#                 pass
    
#     courses = Course.objects.all()
#     context = {'courses': courses}
#     return render(request, 'auth/admin_courses.html', context)



def home(request):
    courses = Course.objects.all()
    services = Services.objects.all()
    context = {'courses': courses, 'services': services}
    return render(request, "auth/index.html", context)

    
def nav(request):
    student = Student.objects.all()
    student = {'studnet': student}
    return render(request, "auth/nav.html", student)
    
def contactus(request):
    return render(request, "auth/contactus.html")
def services(request):
    services = Services.objects.all()
    context = {'services': services}
    return render(request, "auth/services.html" , context)
# def signup(request):
from django.contrib.auth.decorators import login_required

@login_required  # This decorator ensures only logged-in users can access this view
def editprofile(request):
    if request.method == "POST":
        username = request.user.username
        fname = request.POST.get('fname2')
        lname = request.POST.get('lname2')
        email = request.POST.get('email2')
        course = request.POST.get('select2')
        password = request.POST.get('password22')
        batch = request.POST.get('batch2')

        student = Student.objects.get(username=username)
        # Update only the fields that are provided in the form
        student.first_name = fname
        student.last_name = lname
        student.email = email
        student.password = password  # Note: You might want to use set_password() for security.
        student.batch = batch
        student.course_type=course

        # Save the changes to the database
        student.save()

        messages.success(request, "Successfully updated profile")
        return redirect("/index")

    # Save to db
    return render(request, "auth/editprofile.html")

    
def signin(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password) 
        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect('index')
           
        else:
            messages.error(request, "wrong info")
            return redirect('/signup')
    
    
    return render(request, "auth/signin.html")

def signout(request):
   logout(request)
   messages.success(request, "logged out successfully ")
   return render(request,"auth/signin.html") 
   # views.py
# views.py


def enroll(request):
  if request.method == 'POST':
    username = request.POST.get('username') 
    user = Student.objects.get(username=username)
    
    user.active = True
    user.save()

  return redirect('students_detail')
def delete(request):
  if request.method == 'POST':
    username = request.POST.get('username2') 
    user = Student.objects.get(username=username)
    
    user.active = False
    user.save()

  return redirect('students_detail')
# from django.shortcuts import render

# from django.contrib import messages
# from django.shortcuts import redirect, render
# # Create your views here.
def signup(request):
    
    if request.method == "POST" :
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        course = request.POST.get('select')
        password = request.POST.get('password')
        batch = request.POST.get('batch')
        user = User.objects.create_user(username = username, password=password)
        # user.username=username
        # user.password=password
        # user.is_active=TRUE
        student = Student.objects.create(
        user=user,    
        first_name=fname,
        last_name=lname,
        email=email,
        username=username,
        password=password,
        course_type=course,
        batch=batch,
        active=False,
      # Other fields
        )
        
    # Save to db
        student.save()
        messages.success(request,"successfully registered")
        return redirect("/signin")
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, "auth/signup.html" , context)
from .models import Course, CourseFile

# def courses(request):
#     courses = Course.objects.all()
#     context = {'courses': courses}
#     return render(request, 'auth/courses.html', context)


@login_required
def courses(request):
    signed_up_course_name = request.user.student.course_type
    courses = Course.objects.filter(course_name=signed_up_course_name)
    context = {'courses': courses}
    return render(request, 'auth/courses.html', context)
