from django.db import models

# Create your models here.

class student(models.Model):
    rollno=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class course(models.Model):
    student=models.ForeignKey(student,on_delete=models.CASCADE)
    couse_name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)

    def __str__(self):
        return self.couse_name