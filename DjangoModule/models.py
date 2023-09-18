from django.db import models



class Student(models.Model):
    name = models.CharField('name', max_length=200)
    email=models.CharField('email',max_length=100)
    phone=models.CharField('phone',max_length=100)
    roll = models.CharField('roll', max_length=200)
    age=models.IntegerField('age')
    department=models.CharField('department',max_length=100)
   