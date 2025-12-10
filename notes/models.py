from django.db import models

# Create your models here.

class Notes(models.Model):
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

    year = models.CharField(max_length=2, choices=YEAR_CHOICES)
    semester = models.CharField(max_length=2, choices=SEM_CHOICES)
    branch = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=150)
    notes_pdf = models.FileField(upload_to="notes_pdfs/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = "Notes"
        verbose_name_plural = "Notes"

    