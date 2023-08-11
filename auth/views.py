
# from ast import Global
# from gzip import FNAME
# from profile import Profile
# import select
# from ssl import AlertDescription
# from django.http import HttpResponse
# from django.shortcuts import redirect, render
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# # views.py
# from django.contrib.auth.decorators import user_passes_test

# # views.py

# def is_staff_user(user):
#     return user.is_staff

# @user_passes_test(is_staff_user)
# def students_detail(request):
#     # Retrieve all users
#     all_users = User.objects.all()
#     return render(request, 'auth/students_detail.html', {'users': all_users})
# # Create your views here.
# def home(request):
#     return render(request, "auth/index.html")
# def nav(request):
#     return render(request, "auth/nav.html")
# def signup(request):
    
#     if request.method == "POST" :
#         username = request.POST.get('username')
#         fname = request.POST.get('fname')
#         lname = request.POST.get('lname')
#         email = request.POST.get('email')
#         phoneno = request.POST.get('phoneno')
#         password = request.POST.get('password')
        
        
#         myuser = User.objects.create_user(username, email, password,)
#         myuser.first_name = fname
#         myuser.last_name = lname
#         myuser.is_active = False
        
    
#         myuser.save()
        
#         messages.success(request,"successfully registered")
#         return redirect("/signin")
        
#     return render(request, "auth/signup.html")
# def editprofile(request):
    
#     if request.method == "POST" :
#         username = request.POST.get('username2')
#         fname = request.POST.get('fname2')
#         lname = request.POST.get('lname2')
#         email = request.POST.get('email2')
#         phoneno = request.POST.get('phoneno2')
#         password = request.POST.get('password22')
        
#         myuser2 = User.objects.create_user(username, email, password)
#         myuser2.first_name = fname
#         myuser2.last_name = lname
        
#         myuser2.save()
        
#         AlertDescription.success(request,"successfully edited")
#         return redirect("/index")
        
#     return render(request, "auth/editprofile.html")
# def signin(request):
    
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         user = authenticate(username=username, password=password) 
#         if user is not None:
#             login(request, user)
#             fname = user.first_name
#             return render(request,"auth/index.html", {'fname': fname}) 
#         else:
#             messages.error(request, "wrong info")
#             return redirect('/signup')
    
    
#     return render(request, "auth/signin.html")
# def signout(request):
#    logout(request)
#    messages.success(request, "logged out successfully ")
#    return render(request,"auth/signin.html") 
#    # views.py
# # views.py


# def enroll(request):
#   if request.method == 'POST':
#     username = request.POST.get('username') 
#     user = User.objects.get(username=username)
    
#     user.is_active = True
#     user.save()

#   return redirect('students_detail')
# def delete(request):
#   if request.method == 'POST':
#     username = request.POST.get('username2') 
#     user = User.objects.get(username=username)
    
#     user.is_active = False
#     user.save()

#   return redirect('students_detail')