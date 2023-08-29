from django.shortcuts import render, redirect
from django.views import View
from .models import Student
from django.contrib import messages

# Create your views here.


class StudentView(View):
    template_name = 'student/add_student.html'

    def get(self, request):
        all_student = Student.objects.all().order_by('-pk')
        return render(request, 'home/index.html',
                      context={"students": all_student})


class AddStudent(View):
    def get(self, request):
        return render(request, "student/add_student.html")

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        roll = request.POST.get('roll')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        semester = request.POST.get('semester')
        print(name, roll, email, phone, department, semester)

        Student.objects.create(
            student_name=name,
            stident_email=email,
            student_roll=roll,
            student_phone=phone,
            department=department,
            semester=semester,
        )
        messages.success(request, "Student added successfuly!")
        return redirect("/home")
        # return render(request, "student/add_student.html")
