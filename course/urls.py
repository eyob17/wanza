from django.contrib import admin
from django.urls import path, include
from students import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin', admin.site.urls),
    path('',include('auth.urls')),
    path('signup',views.signup, name="signup"),
    path('enroll', views.enroll, name='enroll'),
    path('delete', views.delete, name='delete'),
    path('editprofile', views.editprofile, name='editprofile'),
    path('',views.home, name="index"),
    path('index',views.home, name="index"),
    path('signup',views.signup, name="signup"),
    path('nav',views.nav, name="nav"),
    path('signin',views.signin, name="signin"),
    path('signout',views.signout, name="signout"),
    path('contactus',views.contactus, name="contactus"),
    path('services',views.services, name="services"),
    path('students_detail',views.students_detail, name="students_detail"),
    path('courses',views.courses, name="courses"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)