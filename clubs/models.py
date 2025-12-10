from django.db import models

# Create your models here.
class dataquest(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.IntegerField()
    section = models.CharField(max_length=10)
    year = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=50)
    



class p4p(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.IntegerField()
    year = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    resumeupload = models.FileField(upload_to='resumes/', null=True, blank=True)
    linkedin = models.URLField(max_length=200)
    github = models.URLField(max_length=200)
    