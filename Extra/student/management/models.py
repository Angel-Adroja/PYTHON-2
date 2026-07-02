from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField()
    email=models.EmailField()
    branch=models.CharField()
    