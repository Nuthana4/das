from django.shortcuts import render
from .forms import SearchForm
from .models import syllabus

def syllabus_view(request):
    result = None   # renamed variable

    if request.method == "POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            year = form.cleaned_data['year']
            semester = form.cleaned_data['semester']
            branch = form.cleaned_data['branch']
            subject = form.cleaned_data['subject_name']

            # Use model name (syllabus) and store result in 'result'
            result = syllabus.objects.filter(
                year=year,
                semester=semester,
                branch__iexact=branch,
                subject_name__iexact=subject
            ).first()

    else:
        form = SearchForm()



    return render(request, "syllabus/syllabus.html", {
    "form": form,
    "syllabus": result
})
