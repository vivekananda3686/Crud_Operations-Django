from django.db import models

# Create your models here.

class Student(models.Model):
    roll=models.CharField(max_length=30)
    sname=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    year=models.IntegerField()
    branch=models.CharField(max_length=30)

