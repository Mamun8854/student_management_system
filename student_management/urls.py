from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", views.StudentView.as_view(), name="home_page"),
    path("add/student/", views.AddStudent.as_view(), name="add_student")

]
