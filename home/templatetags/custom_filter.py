from django import template
from home.models import *

register = template.Library()

@register.filter
def getClasss(parentId):
    return Class.objects.filter(interlock_name=parentId)

@register.filter
def getStudents(t1):
    return Student.objects.filter(st_id=t1);


@register.filter
def getStudents1(t1):
    student= Student.objects.filter(st_ten=t1);
    if(student is not None):
        if (len(student) > 0):
            return "true"
    return "false"



