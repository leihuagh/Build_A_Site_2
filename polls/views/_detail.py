from django.shortcuts import render
from polls.models import Question, Choice


def detail(request, id):
    return render(request, 'polls/detail.html', {})
