from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.get_request, name="get_request"),
    path('', views.home_page, name="home_page"),
    path('add-student/', views.add_student, name="add_student"),
    path('admin/', admin.site.urls,name="admin"),
    path('submit/', views.submit_form, name="submit"),
    path("student/",views.student_list,name="student"),
    path("delete-student/<int:param>/",views.delete_student,name="delete-student")
]
