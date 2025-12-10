
from django.urls import path
from .views import question_paper_search

app_name = 'papers'

urlpatterns = [
    path('', question_paper_search, name='question_paper_search'),
]
