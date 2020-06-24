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

    def get_total(self):
        return self.maths + self.sci + self.hindi + self.english + self.sst

    def get_result(self):
        if(self.get_total() >= 300):
            return "1st division"
        elif(self.get_total() >= 250):
            return "2nd division"
        elif(self.get_total() >= 150):
            return "3rd division"
        else:
            return "pappu fail"
