from django.shortcuts import render

# Create your views here.
from .forms import NotesForm
from .models import Notes

def notes_search(request):
    notes = None
    form = NotesForm()

    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            semester = form.cleaned_data['semester']
            branch = form.cleaned_data['branch']
            subject = form.cleaned_data['subject_name']

            # case-insensitive match; get first match if multiple
            notes = Notes.objects.filter(
                year=year,
                semester=semester,
                branch__iexact=branch,
                subject_name__iexact=subject
            ).first()

    

    return render(request, "notes/notes.html", {
    "form": form,
    "notes": notes
})
    
