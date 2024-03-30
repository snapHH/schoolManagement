from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name


class Register(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=130,null=True)
    last_name = models.CharField(max_length=130,null=True)
    email = models.CharField(max_length=130,null=True)
    gen=models.CharField(max_length=30,null=True)
    add=models.CharField(max_length=100,null=True)
    mobile=models.CharField(max_length=10,null=True)
    image=models.FileField(null=True)
    birth=models.DateField(null=True)
    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    reg=models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    position = models.CharField(max_length=100,null=True)
    t_id = models.IntegerField(null=True)

    def __str__(self):
        return self.reg.first_name

class Employee(models.Model):
    reg=models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    position = models.CharField(max_length=100,null=True)
    e_id = models.IntegerField(null=True)

    def __str__(self):
        return self.reg.first_name

class Student(models.Model):
    reg=models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    clas=models.ManyToManyField(Class,null=True, blank=True)
    roll = models.CharField(max_length=100,null=True)
    year = models.IntegerField(null=True)
    s_id = models.IntegerField(null=True)

    def __str__(self):
        return self.reg.first_name+" . "+" . "+self.roll+" . "+str(self.s_id)

class Attendance_Staff(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    a_time = models.TimeField(null=True)
    d_time = models.TimeField(null=True)
    date1 = models.CharField(max_length=30,null=True)
    desc = models.TextField(null=True)

    def __str__(self):
        return self.employee.reg.first_name+" . "+str(self.date1)


class Attendance_Teacher(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    a_time = models.TimeField(null=True)
    d_time = models.TimeField(null=True)
    date1 = models.CharField(max_length=30,null=True)
    desc = models.TextField(null=True)

    def __str__(self):
        return self.teacher.reg.first_name+" . "+str(self.date1)
class Book_Category(models.Model):
    b_cat = models.CharField(max_length=40,null=True)
    def __str__(self):
        return self.b_cat

class Book(models.Model):
    cat = models.ForeignKey(Book_Category,on_delete=models.CASCADE,null=True)
    b_id = models.IntegerField(null=True)
    isbn = models.IntegerField(null=True)
    b_name = models.CharField(max_length=30,null=True)
    author = models.TextField(null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.cat.b_cat+" . "+self.b_name+" . "+self.author


class Fees(models.Model):
    stu = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    remain = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    deposit = models.IntegerField(null=True)
    l_date = models.DateField(null=True)

    def __str__(self):
        return self.stu.reg.first_name+" . "+self.stu.clas+" . "+str(self.stu.roll)

class StudentAttendance(models.Model):
    stu = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    clas = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    shift1 = models.BooleanField(null=True,default=False)
    shift2 = models.BooleanField(null=True,default=False)
    present = models.BooleanField(null=True,default=False)
    attend_date = models.DateField(null=True)

    def __str__(self):
        return self.stu.reg.first_name + " . " + str(self.attend_date)+" . "+ str(self.clas.name)
