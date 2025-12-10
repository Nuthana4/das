from django import forms

class SearchForm(forms.Form):
    YEAR_CHOICES = [
        ('', "Select Year"),
        (1, "1st Year"),
        (2, "2nd Year"),
        (3, "3rd Year"),
        (4, "4th Year"),
    ]

    SEM_CHOICES = [
        ('', "Select Semester"),
        (1, "1st Semester"),
        (2, "2nd Semester"),
    ]
    year = forms.ChoiceField(
        choices=YEAR_CHOICES,
        widget=forms.Select(attrs={
            'class': 'input-select',
            'aria-label': 'Year',
        })
    )
    semester = forms.ChoiceField(
        choices=SEM_CHOICES,
        widget=forms.Select(attrs={
            'class': 'input-select',
            'aria-label': 'Semester',
        })
    )
    branch = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. Computer Science (CSE)',
            'class': 'input-text',
            'aria-label': 'Branch'
        })
    )
    subject_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. Data Structures or DSA',
            'class': 'input-text',
            'aria-label': 'Subject Name'
        })
    )
