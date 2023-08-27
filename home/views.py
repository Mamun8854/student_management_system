from django.shortcuts import render
from django.views import View
from .models import Student
# Create your views here.


class StudentView(View):
    def get(self, request):
        all_student = Student.objects.all()
        return render(request, 'home/index.html',
                      context={"students": all_student})
