from django.shortcuts import render, redirect
from django.views import View
from .models import Student
from django.contrib import messages
from django.views.generic import RedirectView
from django.http import HttpResponse
import datetime
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
# from django.db.models import Sum
# Create your views here.


class StudentView(View):

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


class StudentDeleteView(RedirectView):
    url = "/home"

    def get_redirect_url(self, *args, **kwargs):
        delete_id = kwargs['id']
        Student.objects.get(pk=delete_id).delete()
        return super().get_redirect_url(*args, **kwargs)


class UpdateStudentView(View):
    def get(self, request, id):
        queryset = Student.objects.get(id=id)
        context = {'student': queryset}
        return render(request, 'student/update_student.html', context)

    def post(self, request, id):
        queryset = Student.objects.get(pk=id)
        data = request.POST
        student_name = data.get('name')
        student_email = data.get('email')
        roll = data.get('roll')
        student_mobile = data.get('phone')
        department = data.get('department')
        semester = data.get('semester')

        queryset.student_name = student_name
        queryset.stident_email = student_email
        queryset.student_roll = roll
        queryset.student_phone = student_mobile
        queryset.department = department
        queryset.semester = semester

        queryset.save()
        return redirect('/home')


def Export_pdf(request):
    all_student = Student.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=Student-Info' + \
        str(datetime.datetime.now())+'.pdf'
    response['Content-Transfer-Encoding'] = "binary"
    html_strig = render_to_string(
        'pdf_download/pdf_output.html', {'students': all_student, 'total': 0}
    )
    html = HTML(string=html_strig)
    result = html.write_pdf()
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()

        output = open(output.name, 'rb')
        response.write(output.read())
    return response
