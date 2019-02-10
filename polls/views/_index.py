from django.shortcuts import render
from polls.models import Question, Choice


def index(request):
    questions = Question.objects.all()
    context = {
        'title': 'polls',
        'questions': questions
    }
    return render(request, 'polls/index.html', context)
