"""SchoolManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('login',Login,name="login"),
    path('logout',Logout,name="logout"),
    path('signup',signup,name="signup"),
    path('teacher',teacher,name="addteacher"),
    path('editteacher(?P<pid>[0-9]+)',edit_teacher,name="editteacher"),
    path('student',student,name="addstudent"),
    path('editstudent(?P<pid>[0-9]+)',edit_student,name="editstudent"),
    path('employee',employee,name="addemployee"),
    path('editemployee(?P<pid>[0-9]+)',edit_employee,name="editemployee"),
    path('delete_student(?P<pid>[0-9]+)',delete_student,name="delete_student"),
    path('delete_teacher(?P<pid>[0-9]+)',delete_teacher,name="delete_teacher"),
    path('delete_staff(?P<pid>[0-9]+)',delete_staff,name="delete_staff"),
    path('delete_staff_attendance(?P<pid>[0-9]+)',delete_staff_attendance,name="delete_staff_attendance"),
    path('delete_teacher_attendance(?P<pid>[0-9]+)',delete_teacher_attendance,name="delete_teacher_attendance"),
    path('delete_book(?P<pid>[0-9]+)',delete_book,name="delete_book"),
    
    path('view_teacher',View_Teacher,name="view_teacher"),
    path('add_books',addbooks,name="add_books"),
    path('edit_books(?P<pid>[0-9]+)',edit_books,name="edit_books"),
    path('view_books',View_Books,name="view_books"),
    path('view_employee',View_Employee,name="view_employee"),
    path('view_student',View_Student,name="view_student"),
    path('attendance_staff',attendance_staff,name="attendance_staff"),
    path('view_attendance_staff',View_Attendance_Staff,name="view_attendance_staff"),
    path('attendance_teacher',attendance_teacher,name="attendance_teacher"),
    path('view_attendance_teacher',View_Attendance_Teacher,name="view_attendance_teacher"),
    path('stu',stu,name="stu"),
    path('about',About,name="about"),
    path('contact',Contact,name="contact"),
    path('fee_submit(?P<pid>[0-9]+)',fee_submit,name="fee_submit"),
    path('add_student_attendance',add_student_attendance,name="add_student_attendance"),
    path('add_class',change_class,name="add_class"),
    path('change_class<int:pid>',change_class,name="change_class"),
    path('delete_class<int:pid>',delete_clas,name="delete_class"),
    path('view_class',view_class,name="view_class"),
    path('classwise_attendance',classwise_attendance,name="classwise_attendance"),
    path('studentwise_attendance',studentwise_attendance,name="studentwise_attendance"),
    path('get-student',get_student,name="get_student"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
