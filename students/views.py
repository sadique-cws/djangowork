from django.shortcuts import render
from students.models import *
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from students.forms import StudentForm

class StudentsList(ListView):
    model = Student

class StudentDetails(DetailView):
    model = Student

class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    success_url = "/"

class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = "/"

class StudentDelete(DeleteView):
    model = Student
    success_url = "/"
