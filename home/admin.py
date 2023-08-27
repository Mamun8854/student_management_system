from django.contrib import admin
from home.models import Student
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
