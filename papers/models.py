

# Create your models here.
from django.db import models

# Create your models here.
class QuestionPaper(models.Model):
    YEAR_CHOICES = [
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
        ('4', '4th Year'),
    ]

    SEM_CHOICES = [
        ('1', '1st Semester'),
        ('2', '2nd Semester'),
    ]

    EXAM_TYPE_CHOICES = [
        ('mid1', 'Mid 1'),
        ('mid2', 'Mid 2'),
        ('sem', 'Semester'),
        ('supply', 'Supply'),
    ]

    year = models.CharField(max_length=10, choices=YEAR_CHOICES)
    semester = models.CharField(max_length=10, choices=SEM_CHOICES)
    branch = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=150)
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE_CHOICES)
    pdf_file = models.FileField(upload_to="question_papers/")

    def __str__(self):
        return f"{self.subject_name} - {self.exam_type} - {self.year} Year {self.semester} Sem"
