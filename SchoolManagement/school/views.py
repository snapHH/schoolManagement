import datetime
import json

from dateutil import parser
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *


# Create your views here.
def home(request):
    return render(request,'carousel.html')

def Contact(request):
    return render(request,'contact.html')
def About(request):
    return render(request,'about.html')

def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "login"
            else:
                login(request, user)
                error = "not"
        except:
            error="notlogin"
    d = {'error': error}
    return render(request,'login.html',d)

def Logout(request):
    logout(request)
    return redirect('home')


def signup(request):
    error=False
    if request.method=="POST":
        f=request.POST['fname']
        l=request.POST['lname']
        u=request.POST['uname']
        p=request.POST['pwd']
        ad=request.POST['add']
        m=request.POST['mobile']
        g=request.POST['gen']
        d=request.POST['birth']
        e=request.POST['email']
        i=request.FILES['img']
        user = User.objects.create_user(first_name=f,last_name=l,username=u,password=p,email=e)
        Register.objects.create(user=user,gen=g,add=ad,mobile=m,birth=d,image=i)
        error=True
    d={'error':error}
    return render(request,'signup.html',d)

def teacher(request):
    error=False
    if request.method=="POST":
        f=request.POST['fname']
        l=request.POST['lname']
        ad=request.POST['add']
        m=request.POST['mobile']
        g=request.POST['gen']
        p=request.POST['pos']
        d=request.POST['birth']
        e=request.POST['email']
        i=request.FILES['img']
        reg = Register.objects.create(gen=g,add=ad,mobile=m,birth=d,image=i,first_name=f,last_name=l,email=e)
        Teacher.objects.create(reg=reg,position=p)
        error=True
    d={'error':error}
    return render(request,'teacher.html',d)

def edit_teacher(request,pid):
    error=False
    reg1 = Register.objects.get(id=pid)
    teac=Teacher.objects.get(reg=reg1)
    if request.method=="POST":
        f=request.POST['fname']
        l=request.POST['lname']
        ad=request.POST['add']
        m=request.POST['mobile']
        p=request.POST['pos']
        e=request.POST['email']
        reg1.first_name = f
        reg1.last_name = l
        reg1.email = e
        reg1.add = ad
        reg1.mobile = m
        teac.position = p
        reg1.save()
        teac.save()
        try:
            i = request.FILES['img']
            teac.reg.image = i
            teac.reg.save()
        except:
            pass
        try:
            g = request.POST['gen']
            teac.reg.gen = g
            teac.reg.save()
        except:
            pass
        try:
            d = request.POST['birth']
            teac.reg.birth = d
            teac.reg.save()
        except:
            pass


        error=True
    d={'error':error,'teac':teac}
    return render(request,'edit_teacher.html',d)

def employee(request):
    error=False
    if request.method=="POST":
        f=request.POST['fname']
        l=request.POST['lname']
        ad=request.POST['add']
        m=request.POST['mobile']
        g=request.POST['gen']
        p=request.POST['pos']
        d=request.POST['birth']
        e=request.POST['email']
        i=request.FILES['img']
        reg = Register.objects.create(gen=g,add=ad,mobile=m,birth=d,image=i,first_name=f,last_name=l,email=e)
        Employee.objects.create(reg=reg,position=p)
        error=True
    d={'error':error}
    return render(request,'employee.html',d)

def edit_employee(request,pid):
    error=False
    reg1 = Register.objects.get(id=pid)
    teac=Employee.objects.get(reg=reg1)
    if request.method=="POST":
        f=request.POST['fname']
        l=request.POST['lname']
        ad=request.POST['add']
        m=request.POST['mobile']
        p=request.POST['pos']
        e=request.POST['email']
        teac.reg.first_name = f
        teac.reg.last_name = l
        teac.reg.email = e
        teac.reg.add = ad
        teac.reg.mobile = m
        teac.position = p
        teac.reg.save()
        teac.save()
        try:
            i=request.FILES['imag']
            teac.reg.image = i
            teac.reg.save()
        except:
            pass
        try:
            g=request.POST['gen']
            teac.reg.gen=g
            teac.reg.save()
        except:
            pass
        try:
            d = request.POST['birth']
            teac.reg.birth = d
            teac.reg.save()
        except:
            pass

        error=True

    d={'error':error,'teac':teac}
    return render(request,'edit_employee.html',d)


def student(request):
    clas = Class.objects.all()
    error=False
    if request.method=="POST":
        f=request.POST['fname']
        l=request.POST['lname']
        ad=request.POST['add']
        m=request.POST['mobile']
        g=request.POST['gen']
        r=request.POST['roll']
        y=request.POST['year']
        d=request.POST['birth']
        e=request.POST['email']
        i=request.FILES['img']
        reg = Register.objects.create(gen=g,add=ad,mobile=m,birth=d,image=i,first_name=f,last_name=l,email=e)
        stu=Student.objects.create(reg=reg,roll=r,year=y)
        stu.clas.set(request.POST.getlist('clas'))
        stu.save()
        Fees.objects.create(stu=stu,deposit=0,total=50000,remain=50000)
        error=True
    d={'error':error,'clas':clas}
    return render(request,'student.html',d)

def edit_student(request,pid):
    error=False
    clas = Class.objects.all()
    reg1 = Register.objects.get(id=pid)
    teac=Student.objects.get(reg=reg1)
    if request.method=="POST":
        f=request.POST['fname']
        l=request.POST['lname']
        ad=request.POST['add']
        m=request.POST['mobile']
        e=request.POST['email']
        r = request.POST['roll']
        y = request.POST['year']
        reg1.first_name = f
        reg1.last_name = l
        reg1.email = e
        reg1.add = ad
        reg1.mobile = m
        teac.clas.set(request.POST.getlist('clas'))
        teac.roll = r
        teac.year = y
        reg1.save()
        teac.save()
        try:
            i = request.FILES['img']
            teac.reg.image = i
            teac.reg.save()
        except:
            pass
        try:
            g=request.POST['gen']
            reg1.gen=g
            reg1.save()
        except:
            pass
        try:
            d = request.POST['birth']
            reg1.birth=d
            reg1.save()
        except:
            pass

        error=True
    d={'error':error,'teac':teac,'clas':clas}
    return render(request,'edit_student.html',d)

def attendance_staff(request):
    error=False
    reg = Employee.objects.all()
    today1 =datetime.date.today()
    if request.method=="POST":
        f=request.POST['fname']
        a=request.POST['a_time']
        de=request.POST['d_time']
        des=request.POST['desc']
        d=request.POST['date']
        reg1 = Register.objects.get(id=f)
        emp = Employee.objects.get(reg=reg1)
        Attendance_Staff.objects.create(employee=emp,a_time=a,d_time=de,desc=des,date1=d)
        error=True
    d={'error':error,'today':today1,'reg':reg}
    return render(request,'attendance_staff.html',d)

def attendance_teacher(request):
    error=False
    reg = Teacher.objects.all()
    today1 =datetime.date.today()
    if request.method=="POST":
        f=request.POST['fname']
        a=request.POST['a_time']
        de=request.POST['d_time']
        des=request.POST['desc']
        d=request.POST['date']
        reg1 = Register.objects.get(id=f)
        tea = Teacher.objects.get(reg=reg1)
        Attendance_Teacher.objects.create(teacher=tea,a_time=a,d_time=de,desc=des,date1=d)
        error=True
    d={'error':error,'today':today1,'reg':reg}
    return render(request,'attendance_teacher.html',d)


def addbooks(request):
    error=False
    cat = Book_Category.objects.all()
    if request.method=="POST":
        c=request.POST['cat']
        a=request.POST['auth']
        i=request.POST['isbn']
        b=request.POST['b_name']
        bi=request.POST['bid']
        im=request.FILES['image']
        cat1 = Book_Category.objects.filter(b_cat=c).first()
        Book.objects.create(cat=cat1,author=a,isbn=i,b_name=b,b_id=bi,image=im)
        error=True
    d={'error':error,'cat':cat}
    return render(request,'addbooks.html',d)

def edit_books(request,pid):
    error=False
    cat = Book_Category.objects.all()
    data = Book.objects.get(id=pid)
    if request.method=="POST":
        c=request.POST['cat']
        a=request.POST['auth']
        i=request.POST['isbn']
        b=request.POST['b_name']
        bi=request.POST['bid']
        try:
            im=request.FILES['image']
            data.image=im
            data.save
        except:
            pass
        cat1 = Book_Category.objects.filter(b_cat=c).first()
        data.cat = cat1
        data.b_name=b
        data.isbn=i
        data.author=a
        data.b_id=bi
        data.save()
        error=True
    d={'error':error,'cat':cat,'data':data}
    return render(request,'edit_books.html',d)

def View_Teacher(request):
    tea = Teacher.objects.all()
    d ={'tea':tea}
    return render(request,'view_teacher.html',d)

def View_Employee(request):
    tea = Employee.objects.all()
    d ={'tea':tea}
    return render(request,'view_employee.html',d)

def View_Student(request):
    stu = Student.objects.all()
    d ={'stu':stu}
    return render(request,'view_student.html',d)

def View_Attendance_Staff(request):
    stu = Attendance_Staff.objects.all()
    d ={'tea':stu}
    return render(request,'view_attendance_staff.html',d)


def View_Books(request):
    stu = Book.objects.all()
    d ={'book':stu}
    return render(request,'view_books.html',d)

def View_Attendance_Teacher(request):
    stu = Attendance_Teacher.objects.all()
    d ={'stu':stu}
    return render(request,'view_attendance_teacher.html',d)

def stu(request):
    st=Student.objects.all()
    if request.method=="POST":
        try:
            i=request.POST['s_id']
            stu = Student.objects.filter(s_id=i).first()
            fee = Fees.objects.get(stu=stu)
            return redirect('fee_submit', fee.id)

        except:
            pass
    d={'stu':st}
    return render(request,'fees.html',d)

def fee_submit(request,pid):
    st=Student.objects.all()
    fee=Fees.objects.get(id=pid)
    today1 = datetime.date.today()
    f1=0
    if request.method=="POST":
        try:
            i = request.POST['s_id']
        except:
            pass
        d=request.POST['depo']
        f1 = fee.remain
        fee.remain=fee.remain-10000
        fee.deposit=d
        fee.l_date=today1
        fee.save()
    d ={'data':fee,'today':today1,'stu':st,'f1':f1}
    return render(request,'fees.html',d)

def delete_student(request,pid):
    data=Student.objects.get(id=pid)
    data.delete()
    return redirect('view_student')

def delete_teacher(request,pid):
    data=Teacher.objects.get(id=pid)
    data.delete()
    return redirect('view_teacher')

def delete_staff(request,pid):
    data=Employee.objects.get(id=pid)
    data.delete()
    return redirect('view_employee')

def delete_book(request,pid):
    data=Book.objects.get(id=pid)
    data.delete()
    return redirect('view_books')

def delete_staff_attendance(request,pid):
    data=Attendance_Staff.objects.get(id=pid)
    data.delete()
    return redirect('view_attendance_staff')

def delete_teacher_attendance(request,pid):
    data=Attendance_Teacher.objects.get(id=pid)
    data.delete()
    return redirect('view_attendance_teacher')

def add_student_attendance(request):
    clas = request.GET.get('class',None)
    clas_data = None
    student = None
    if clas:
        clas_data = Class.objects.get(id=clas)
        student = Student.objects.filter(clas=clas_data)
    clas_data1 = Class.objects.all()

    attend = StudentAttendance.objects.filter(attend_date=datetime.date.today(),clas=clas_data)
    shift=request.GET.get('shift',None)
    print(shift,555555)
    shift1, shift2 = False, False
    if shift == "Shift-1":
        shift1 = True
        attend1 = attend.filter(shift1=shift1).first()
        if attend1:
            mesage = messages.success(request,clas_data.name+" class "+shift+" attendance is already marked")
        # else:
        #     mesage = messages.success(request, clas_data.name + " class " + shift + " data not found")
    elif shift == "Shift-2":
        shift2 = True
        attend1 = attend.filter(shift2=shift2).first()
        if attend1:
            mesage = messages.success(request,clas_data.name+" class "+shift+" attendance is already marked")
        # else:
        #     mesage = messages.success(request, clas_data.name + " class " + shift + " data not found")
    if request.method=="POST":
        for i in range(1,student.count()+1):
            a = request.POST.get('attendance-'+str(i))
            persent = False
            if a == "True":
                persent = True
            b = request.POST.get('pid-'+str(i),None)
            student1 = Student.objects.get(id=b)
            attend = StudentAttendance.objects.create(shift1=shift1, shift2=shift2, present=persent, stu=student1, clas=clas_data, attend_date=datetime.date.today())
        messages.success(request, "Today " +clas_data.name+" class "+shift + "attendance marked.")
    return render(request, 'add_student_attendance.html',{'student':student, 'clas_data1':clas_data1})

def change_class(request, pid=None):
    clas = None
    clas1 = None
    if pid:
        clas = Class.objects.filter(id=pid)
        clas1 = clas.first()
    if request.method == "POST":
        c = request.POST['cname']
        if pid:
            clas1 = clas.update(name=c)
            message = messages.success(request,'Data Update successfully')
        else:
            clas1 = Class.objects.create(name=c)
            message = messages.success(request, 'Data Added successfully')
    d = {'clas':clas1}
    return render(request,'add_class.html',d)

def view_class(request):
    clas = Class.objects.all()
    d = {'clas':clas}
    return render(request,'view_class.html',d)

def delete_clas(request,pid):
    clas = Class.objects.get(id=pid)
    clas.delete()
    messages.success(request,'Class Deleted Successfully')
    return redirect('view_class')

def classwise_attendance(request):
    clas1 = Class.objects.all()
    clas = request.GET.get('class', None)
    sdate = request.GET.get('sdate', None)
    edate = request.GET.get('edate', None)
    attend2 = None
    if clas and sdate and edate:
        attend = StudentAttendance.objects.filter(attend_date__range=(parser.parse(sdate), parser.parse(edate)) ,clas=Class.objects.get(id=clas))
        attend2 = attend.values('attend_date','clas').annotate(total=Count('present'))
        if not attend:
            messages.success(request,'Data not found')
    return render(request, 'classwise_attendance.html',{'attend':attend2,'clas1':clas1})

def studentwise_attendance(request):
    clas1 = Class.objects.all()
    clas = request.GET.get('class', None)
    student = request.GET.get('student', None)
    sdate = request.GET.get('sdate', None)
    edate = request.GET.get('edate', None)
    attend = None
    if clas and sdate and edate and student:
        student = Student.objects.get(id=student)
        attend = StudentAttendance.objects.filter(stu=student, present=True, attend_date__range=(parser.parse(sdate), parser.parse(edate)) ,clas=Class.objects.get(id=clas))
        attend = attend.values('attend_date').annotate(Count('present'))
        if not attend:
            messages.success(request,'Data not found')
    return render(request, 'studentwise_attendance.html',{'attend':attend,'clas1':clas1,'student':student})

def get_student(request):
    clas = request.GET.get('class_choice')
    student = Student.objects.filter(clas=Class.objects.get(id=clas))
    data = []
    data1 = []
    for i in student:
        data.append(i.id)
        data1.append(i.reg.first_name)
    d = dict(zip(data, data1))
    return HttpResponse(json.dumps(d), content_type="application/json")