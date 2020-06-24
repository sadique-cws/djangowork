from django.shortcuts import render
from students.models import *
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView,UpdateView,CreateView


class StudentsList(ListView):
    model = Student

class StudentDetails(DetailView):
    model = Student

class StudentCreate(CreateView):
    model = Student

class StudentUpdate(UpdateView):
    model = Student

class StudentDelete(DeleteView):
    model = Student
