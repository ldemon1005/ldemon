from django.shortcuts import render
from home.models import *

# Create your views here.
def index(request):
    interlock=Interlock.objects.all()
    classs=Class.objects.filter()
    student=Student.objects.all()
    contex = {
        "interlock": interlock,
        "Student":student
    }
    return render(request, "home/index.html",contex )

def index1(request):
    interlock=Interlock.objects.all()
    classs=Class.objects.filter()
    student=Student.objects.all()
    contex = {
        "interlock": interlock,
        "Student":student
    }
    return render(request, "home/index1.html",contex )

def search(request):

    contex = {
    }
    return render(request, "home/student.html", contex)

def student(request):
    contex={
    }
    return render(request, "home/student.html",contex)
def student1(request):
    interlock = Interlock.objects.all()
    classs = Class.objects.filter()
    x=request.GET.get("user","")
    student1 = Student.objects.filter(st_ten__contains=x )
    contex = {
        "interlock": interlock,
        "Student1": student1
    }
    return render(request, "home/student1.html",contex)