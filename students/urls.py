"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students.views import *
urlpatterns = [
    path('', StudentsList.as_view(),name="student_list"),
    path('create', StudentCreate.as_view(),name="student_create"),
    path('update/<int:pk>', StudentUpdate.as_view(),name="student_update"),
    path('delete/<int:pk>', StudentDelete.as_view(),name="student_delete"),
    path('details/<int:pk>', StudentDetails.as_view(),name="student_details"),
]
