from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", views.StudentView.as_view(), name="home_page"),
    path("add/student/", views.AddStudent.as_view(), name="add_student"),
    path(
        "delete/student/<int:id>/", views.StudentDeleteView.as_view(),
        name="delete_student"),
    path(
        "update/student/<int:id>/", views.UpdateStudentView.as_view(),
        name="update_student"),
    path(
        "export-pdf", views.Export_pdf,
        name="export_pdf")

]
