from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contact = models.IntegerField(default=0)
    city = models.CharField(max_length=200)
    maths = models.IntegerField(default=0)
    sci = models.IntegerField(default=0)
    sst = models.IntegerField(default=0)
    hindi = models.IntegerField(default=0)
    english = models.IntegerField(default=0)

