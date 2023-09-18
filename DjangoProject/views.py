from django.shortcuts import render,redirect
from django.template import loader
from DjangoModule.models import Student
from django.http import HttpResponse,HttpRequest


def get_request(request):
    if request.method=="GET":
        print("This is Get Request")
    return HttpResponse("First Django App Creation Successfull")

def home_page(request):
    try:
        temp=loader.get_template('home.html')
        context={"content":"Welcome to Our Django Web App"}
        return HttpResponse(temp.render(context,request))
    except Exception as e:
        return "Internal Server Error"

def add_student(request):
    try:
        temp=loader.get_template("add_student.html")
        context={"content":"Welcome to Our Django Web App"}
        return HttpResponse(temp.render(context,request))
    except Exception as e:
        return "Internal Server Error"
def student_list(request):
    try:
        student=Student.objects.all().values()
        context={"students":student}
        temp=loader.get_template("student.html")
        return HttpResponse(temp.render(context,request))
    except Exception as e:
        return "Internal Server Error"
def delete_student(request,param):
    try:
        student = Student.objects.get(id=param)
        student.delete()
        return redirect("/student")
    except Exception as e:
        return "Internal Server Error"

def submit_form(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            roll = request.POST.get('roll')
            age = request.POST.get('age')
            department = request.POST.get('department')
            request_body = request.body.decode('utf-8')
            print(request_body)
            contact = Student(name=name, email=email, phone=phone,department=department,age=age,roll=roll)
            contact.save()
            return redirect("/student")
    except Exception as e:
        return "Internal Server Error"
