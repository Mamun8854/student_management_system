from django.contrib import admin
from home.models import Student, Employee
# Register your models here.


@admin.register(Student)
class studentModelAdmin(admin.ModelAdmin):
    list_display = [
        "student_name",
        "stident_email",
        "student_roll",
        "student_phone",
        "department",
        "semester"
    ]


@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = [
        "employee_name",
        "employee_email",
        "employee_phone",
        "employee_address"
    ]
