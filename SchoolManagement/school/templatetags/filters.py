from dateutil import parser
from django import template
from school.models import *
register = template.Library()

@register.simple_tag
def get_present_attendance(dat, clas, shift):
    # clas = Class.objects.get(id=clas)
    shift1 ,shift2 = False, False
    if shift == 'shift1':
        shift1 = True
    elif shift == 'shift2':
        shift2 = True
    attend = StudentAttendance.objects.filter(clas=clas, attend_date=dat, shift1=shift1, shift2=shift2, present=True)
    return attend.count()

@register.simple_tag
def get_absent_attendance(dat, clas, shift):
    # clas = Class.objects.get(id=clas)
    shift1 ,shift2 = False, False
    if shift == 'shift1':
        shift1 = True
    elif shift == 'shift2':
        shift2 = True
    attend = StudentAttendance.objects.filter(clas=clas, attend_date=dat, shift1=shift1, shift2=shift2, present=False)
    return attend.count()

@register.simple_tag
def get_total_present(request, shift):
    clas = Class.objects.get(id=int(request.GET.get('class')))
    shift1 ,shift2 = False, False
    if shift == 'shift1':
        shift1 = True
    elif shift == 'shift2':
        shift2 = True
    attend = StudentAttendance.objects.filter(clas=clas, attend_date__range=(request.GET.get('sdate'), request.GET.get('edate')), shift1=shift1, shift2=shift2, present=True)
    return attend.count()

@register.simple_tag
def get_total_absent(request, shift):
    clas = Class.objects.get(id=int(request.GET.get('class')))
    shift1, shift2 = False, False
    if shift == 'shift1':
        shift1 = True
    elif shift == 'shift2':
        shift2 = True
    attend = StudentAttendance.objects.filter(clas=clas, attend_date__range=(parser.parse(request.GET.get('sdate')), parser.parse(request.GET.get('edate'))),shift1=shift1, shift2=shift2, present=False)
    return attend.count()

@register.simple_tag
def get_shift_present(request, shift, attend_date):
    clas = Class.objects.get(id=int(request.GET.get('class')))
    student = Student.objects.get(id=int(request.GET.get('student')))
    shift1, shift2 = False, False
    if shift == 'shift1':
        shift1 = True
    elif shift == 'shift2':
        shift2 = True
    attend = StudentAttendance.objects.filter(clas=clas,stu=student, attend_date=attend_date,shift1=shift1, shift2=shift2, present=True)

    if attend:
        return "Present"
    else:
        return "Absent"

@register.simple_tag
def get_class_name(obj):
    clas = Class.objects.get(id=obj)
    return clas.name

register.filter('get_absent_attendance',get_absent_attendance)
register.filter('get_present_attendance',get_present_attendance)
register.filter('get_total_absent',get_total_absent)
register.filter('get_total_present',get_total_present)
register.filter('get_class_name',get_class_name)
register.filter('get_shift_present',get_shift_present)