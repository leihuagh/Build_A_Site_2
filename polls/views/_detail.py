from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice


def detail(request, id):
    question = get_object_or_404(Question, id=id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)
