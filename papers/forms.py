from django import forms

class QuestionPaperForm(forms.Form):
    YEAR_CHOICES = [
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
        ('4', '4th Year')
    ]

    SEM_CHOICES = [
        ('1', '1st Semester'),
        ('2', '2nd Semester'),
    ]

    EXAM_CHOICES = [
        ('mid1', 'Mid 1'),
        ('mid2', 'Mid 2'),
        ('sem', 'Semester'),
        ('supply', 'Supply'),
    ]

    year = forms.ChoiceField(choices=YEAR_CHOICES)
    semester = forms.ChoiceField(choices=SEM_CHOICES)
    branch = forms.CharField(max_length=50)
    subject_name = forms.CharField(max_length=100)
    exam_type = forms.ChoiceField(choices=EXAM_CHOICES)
