from django.contrib import admin
from django.urls import path
from .views import StudentCurd

urlpatterns = [
    path('students', StudentCurd.as_view(), name="students_list_or_create"),
    path('students/<int:pk>/', StudentCurd.as_view(), name="students_get_or_update"),

]