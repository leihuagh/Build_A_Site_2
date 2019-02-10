from django.shortcuts import render
from polls.models import Question, Choice


def index(request):
    return render(request, 'polls/index.html', {})
