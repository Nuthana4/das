from django.db import models


# Create your models here.

class syllabus(models.Model):
    YEAR_CHOICES = [
        (1, "1st Year"),
        (2, "2nd Year"),
        (3, "3rd Year"),
        (4, "4th Year"),
    ]

    SEM_CHOICES = [
        (1, "1st Semester"),
        (2, "2nd Semester"),
    ]

    year = models.IntegerField(choices=YEAR_CHOICES)
    semester = models.IntegerField(choices=SEM_CHOICES)
    branch = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='syllabus_pdfs/')

  