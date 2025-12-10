

# Create your views here.
from django.shortcuts import render

# Create your views here.
from .models import QuestionPaper
from .forms import QuestionPaperForm

def question_paper_search(request):
    results = None
    form = QuestionPaperForm()

    if request.method == "POST":
        form = QuestionPaperForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data["year"]
            semester = form.cleaned_data["semester"]
            branch = form.cleaned_data["branch"]
            subject = form.cleaned_data["subject_name"]
            exam = form.cleaned_data["exam_type"]

            results = QuestionPaper.objects.filter(
                year=year,
                semester=semester,
                branch__iexact=branch,
                subject_name__iexact=subject,
                exam_type=exam
            ).first()

    


    return render(request, "papers/papers.html", {
    "form": form,
    "results": results
})
