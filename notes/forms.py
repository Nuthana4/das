from django import forms

class NotesForm(forms.Form):
    YEAR_CHOICES = [('1','1st Year'),('2','2nd Year'),('3','3rd Year'),('4','4th Year')]
    SEM_CHOICES = [('1','1st Semester'),('2','2nd Semester')]

    year = forms.ChoiceField(choices=YEAR_CHOICES, widget=forms.Select(attrs={'class':'input'}))
    semester = forms.ChoiceField(choices=SEM_CHOICES, widget=forms.Select(attrs={'class':'input'}))
    branch = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'input','placeholder':'e.g. CSE'}))
    subject_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input','placeholder':'e.g. DBMS'}))
